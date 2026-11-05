/**
 * REWAVE Pour Player
 * 
 * Maps ScrollTrigger progress to the Blender-authored pour sequence (rewave_pour_rig.json).
 * Drives productGroup (position, quaternion) and capMeshRoot (local position, quaternion)
 * with zero per-frame memory allocation.
 *
 * Future Liquid Integration Hook:
 *   liquidUrl: 'assets/pour/liquid_frames'
 *   (fail-soft, disabled until liquid files exist)
 */

export class RewavePour {
  constructor(o = {}) {
    this.T = o.THREE || (typeof window !== 'undefined' ? window.THREE : null);
    if (!this.T) {
      throw new Error('RewavePour: THREE must be provided in constructor options or on window.THREE');
    }

    Object.assign(this, {
      scene: null,
      productGroup: null,
      capMesh: null,
      juiceMesh: null,
      rigUrl: 'assets/pour/rewave_pour_rig.json',
      liquidUrl: 'assets/pour/liquid_frames',
      loadLiquid: false, // Disabled until liquid files exist (fail-soft)
      deferLiquid: false,
      liquidMaterial: null,
      firstFrame: 1,
      lastFrame: 240,
      streamStretch: 1,
      worldScale: 1 // bottle scale / authoring scale (0.038): scales bottle travel + liquid together
    }, o);

    this.rig = null;
    this.meta = null;
    this.bin = null;
    this.geo = null;
    this.mesh = null;
    this.juicePlane = null;
    this._lastLiquidFrame = -1;

    // Pre-allocated math objects (ZERO allocations during setProgress / setFrame)
    this._qBottle0 = new this.T.Quaternion();
    this._qBottle1 = new this.T.Quaternion();
    this._qCap0 = new this.T.Quaternion();
    this._qCap1 = new this.T.Quaternion();
    this._qRest = new this.T.Quaternion(0, 0, 0, 1);
    this._qCapRest = new this.T.Quaternion(0, 0.688195, 0, 0.725526);
    this._vRest = new this.T.Vector3(0, -0.22, 0);
    this._vCapRest = new this.T.Vector3(-0.0226, 31.5695, -0.0012);
  }

  async load() {
    const T = this.T;

    // 1. Load rig JSON (bottle & cap keyframes)
    const rigRes = await fetch(this.rigUrl);
    if (!rigRes.ok) {
      throw new Error(`RewavePour: Failed to fetch rig from ${this.rigUrl} (status ${rigRes.status})`);
    }
    this.rig = await rigRes.json();
    this.firstFrame = this.rig.frameStart || 1;
    this.lastFrame = this.rig.frameEnd || 240;

    // Record initial rest values from Frame 1
    if (this.rig.frames && this.rig.frames.length > 0) {
      const f1 = this.rig.frames[0];
      this._vRest.set(f1.bottle.p[0], f1.bottle.p[1], f1.bottle.p[2]);
      this._qRest.fromArray(f1.bottle.q);
      if (f1.capLocal) {
        this._vCapRest.set(f1.capLocal.p[0], f1.capLocal.p[1], f1.capLocal.p[2]);
        this._qCapRest.fromArray(f1.capLocal.q);
      }
    }

    // 2. Setup dynamic juice level horizontal clipping plane
    if (this.juiceMesh && this.juiceMesh.material) {
      // Normal points downwards (0, -1, 0) so material above the constant level is clipped away
      this.juicePlane = new T.Plane(new T.Vector3(0, -1, 0), 100);
      const mats = Array.isArray(this.juiceMesh.material) ? this.juiceMesh.material : [this.juiceMesh.material];
      mats.forEach(m => {
        m.clippingPlanes = [this.juicePlane];
        m.clipShadows = true;
      });
    }

    if (this.loadLiquid && !this.deferLiquid) await this.loadLiquidSequence();

    return this;
  }


  /** Optional, fail-soft liquid sequence download (called in idle time by the page). */
  async loadLiquidSequence() {
    const T = this.T;
    if (this.mesh || !this.liquidUrl) return this;
    // Clearly marked integration point: assets/pour/liquid_frames (.json, .bin/.bin.gz)
    {
      try {
        const metaRes = await fetch(this.liquidUrl + '.json');
        if (metaRes.ok) {
          const meta = await metaRes.json();
          this.meta = meta;

          let buf = null;
          try {
            const gzRes = await fetch(this.liquidUrl + '.bin.gz');
            if (gzRes.ok && typeof DecompressionStream !== 'undefined') {
              buf = await new Response(gzRes.body.pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
            }
          } catch (e) {}

          if (!buf) {
            const binRes = await fetch(this.liquidUrl + '.bin');
            if (binRes.ok) buf = await binRes.arrayBuffer();
          }

          if (buf && meta.frames && meta.frames.length > 0) {
            this.bin = buf;
            const maxV = Math.max(...meta.frames.map(f => f.v || 0));
            const maxT = Math.max(...meta.frames.map(f => f.t || 0));
            if (maxV > 0 && maxT > 0) {
              const g = new T.BufferGeometry();
              g.setAttribute('position', new T.BufferAttribute(new Float32Array(maxV * 3), 3).setUsage(T.DynamicDrawUsage));
              g.setAttribute('normal', new T.BufferAttribute(new Float32Array(maxV * 3), 3).setUsage(T.DynamicDrawUsage));
              g.setIndex(new T.BufferAttribute(new Uint32Array(maxT * 3), 1).setUsage(T.DynamicDrawUsage));
              g.boundingSphere = new T.Sphere(new T.Vector3(1.5, -3.5, 0), 9);
              this.geo = g;

              const mat = this.liquidMaterial || new T.MeshPhysicalMaterial({
                color: 0xdff0c4, transmission: 1.0, ior: 1.345, roughness: 0.02, thickness: 0.25,
                attenuationColor: new T.Color(0x8cc94a), attenuationDistance: 1.4, envMapIntensity: 1.2,
                transparent: true, side: T.FrontSide
              });

              this.mesh = new T.Mesh(g, mat);
              this.mesh.frustumCulled = false;
              this.mesh.renderOrder = 5;
              this.mesh.visible = false;
              if (this.scene) this.scene.add(this.mesh);
            }
          }
        }
      } catch (err) {
        // Fail-soft: continue without liquid sequence
        console.warn('RewavePour: Optional liquid sequence not loaded (fail-soft):', err.message);
      }
    }

    return this;
  }

  frameFromProgress(p) {
    const clamped = Math.min(1, Math.max(0, p));
    return this.firstFrame + clamped * (this.lastFrame - this.firstFrame);
  }

  _decodeLiquid(frame) {
    if (!this.mesh || !this.geo || !this.meta || !this.bin) return;
    const rec = this.meta.frames[frame - this.meta.frames[0].f];
    if (!rec || rec.v === 0) {
      this.mesh.visible = false;
      return;
    }
    if (frame === this._lastLiquidFrame) return;
    this._lastLiquidFrame = frame;

    const dv = new DataView(this.bin, rec.o);
    const nV = dv.getUint32(0, true), nT = dv.getUint32(4, true);
    let o = rec.o + 8;
    const q = new Uint16Array(this.bin, o, nV * 3); o += nV * 6;
    const n8 = new Int8Array(this.bin, o, nV * 2); o += nV * 2;
    if (o % 4) o += 4 - (o % 4);
    const idx = new Uint16Array(this.bin, o, nT * 3);
    const mn = this.meta.bboxMin, ex = this.meta.bboxExtent;
    const P = this.geo.attributes.position.array;
    const N = this.geo.attributes.normal.array;
    const I = this.geo.index.array;

    for (let i = 0; i < nV; i++) {
      const bx = mn[0] + (q[i * 3] / 65535) * ex[0];
      const by = mn[1] + (q[i * 3 + 1] / 65535) * ex[1];
      const bz = mn[2] + (q[i * 3 + 2] / 65535) * ex[2];
      P[i * 3] = bx; P[i * 3 + 1] = bz; P[i * 3 + 2] = -by;

      let ox = n8[i * 2] / 127, oy = n8[i * 2 + 1] / 127;
      const oz = 1 - Math.abs(ox) - Math.abs(oy);
      if (oz < 0) {
        const t = ox;
        ox = (1 - Math.abs(oy)) * Math.sign(t || 1);
        oy = (1 - Math.abs(t)) * Math.sign(oy || 1);
      }
      const l = Math.hypot(ox, oy, oz) || 1;
      N[i * 3] = ox / l; N[i * 3 + 1] = oz / l; N[i * 3 + 2] = -oy / l;
    }

    for (let i = 0; i < nT * 3; i += 3) {
      I[i] = idx[i];
      I[i + 1] = idx[i + 2];
      I[i + 2] = idx[i + 1];
    }

    this.geo.attributes.position.needsUpdate = true;
    this.geo.attributes.normal.needsUpdate = true;
    this.geo.index.needsUpdate = true;
    this.geo.setDrawRange(0, nT * 3);
    this.mesh.visible = true;
  }

  /**
   * Applies rig at exact frame (supports sub-frame interpolation)
   * Zero per-frame memory allocation.
   */
  setFrame(fr) {
    if (!this.rig || !this.rig.frames) return { frame: fr, camY: 0 };
    fr = Math.min(this.lastFrame, Math.max(this.firstFrame, fr));

    const f0 = Math.floor(fr);
    const f1 = Math.min(this.lastFrame, f0 + 1);
    const t = fr - f0;

    const idx0 = f0 - this.rig.frameStart;
    const idx1 = f1 - this.rig.frameStart;
    const A = this.rig.frames[idx0];
    const B = this.rig.frames[idx1];

    // Bottle position (world)
    if (this.productGroup) {
      const bx = A.bottle.p[0] + (B.bottle.p[0] - A.bottle.p[0]) * t;
      const by = A.bottle.p[1] + (B.bottle.p[1] - A.bottle.p[1]) * t;
      const bz = A.bottle.p[2] + (B.bottle.p[2] - A.bottle.p[2]) * t;
      const ws = this.worldScale;
      this.productGroup.position.set(bx * ws, by * ws, bz * ws);

      // Bottle rotation (view-axis tilt quaternion)
      this._qBottle0.fromArray(A.bottle.q);
      this._qBottle1.fromArray(B.bottle.q);
      this.productGroup.quaternion.copy(this._qBottle0.slerp(this._qBottle1, t));
    }

    // Cap position & rotation (local to bottle root)
    if (this.capMesh && A.capLocal && B.capLocal) {
      const cx = A.capLocal.p[0] + (B.capLocal.p[0] - A.capLocal.p[0]) * t;
      const cy = A.capLocal.p[1] + (B.capLocal.p[1] - A.capLocal.p[1]) * t;
      const cz = A.capLocal.p[2] + (B.capLocal.p[2] - A.capLocal.p[2]) * t;
      this.capMesh.position.set(cx, cy, cz);

      this._qCap0.fromArray(A.capLocal.q);
      this._qCap1.fromArray(B.capLocal.q);
      this.capMesh.quaternion.copy(this._qCap0.slerp(this._qCap1, t));
    }

    // Horizontal juice level clipping plane
    if (this.juicePlane && A.juiceY !== undefined && B.juiceY !== undefined) {
      this.juicePlane.constant = A.juiceY + (B.juiceY - A.juiceY) * t;
    }

    // Liquid mesh sequence (if loaded)
    if (this.mesh) this.mesh.scale.set(this.worldScale, this.worldScale * (this.streamStretch || 1), this.worldScale);   // stretch about the neck (y = 0)
    this._decodeLiquid(Math.round(fr));

    this.currentFrame = fr;
    const camY = A.camY + (B.camY - A.camY) * t;
    return { frame: fr, camY };
  }

  /**
   * Maps progress 0..1 to the full timeline (frame 1..240)
   */
  setProgress(p) {
    return this.setFrame(this.frameFromProgress(p));
  }

  /**
   * Smoothly blends the bottle and cap from a source rig frame to rest pose
   * blendT: 0.0 (full source frame) -> 1.0 (full rest pose)
   */
  blendToRest(sourceFrame, blendT) {
    if (!this.rig || !this.rig.frames) return;
    const bT = Math.min(1, Math.max(0, blendT));
    if (bT <= 0) {
      this.setFrame(sourceFrame);
      return;
    }

    const idx = Math.min(this.rig.frames.length - 1, Math.max(0, Math.round(sourceFrame) - this.rig.frameStart));
    const A = this.rig.frames[idx];

    if (this.productGroup) {
      const bx = A.bottle.p[0] + (this._vRest.x - A.bottle.p[0]) * bT;
      const by = A.bottle.p[1] + (this._vRest.y - A.bottle.p[1]) * bT;
      const bz = A.bottle.p[2] + (this._vRest.z - A.bottle.p[2]) * bT;
      this.productGroup.position.set(bx, by, bz);

      this._qBottle0.fromArray(A.bottle.q);
      this.productGroup.quaternion.copy(this._qBottle0.slerp(this._qRest, bT));
    }

    if (this.capMesh && A.capLocal) {
      const cx = A.capLocal.p[0] + (this._vCapRest.x - A.capLocal.p[0]) * bT;
      const cy = A.capLocal.p[1] + (this._vCapRest.y - A.capLocal.p[1]) * bT;
      const cz = A.capLocal.p[2] + (this._vCapRest.z - A.capLocal.p[2]) * bT;
      this.capMesh.position.set(cx, cy, cz);

      this._qCap0.fromArray(A.capLocal.q);
      this.capMesh.quaternion.copy(this._qCap0.slerp(this._qCapRest, bT));
    }

    if (this.juicePlane && A.juiceY !== undefined) {
      const restJuiceY = this.rig.frames[0].juiceY || 1.1906;
      this.juicePlane.constant = A.juiceY + (restJuiceY - A.juiceY) * bT;
    }
  }
}

// Expose on window for vanilla script compatibility
if (typeof window !== 'undefined') {
  window.RewavePour = RewavePour;
}

export default RewavePour;
