# REWAVE — Cinematic Pour: Integration Notes (work-in-progress checkpoint)

Status legend: **DONE** = built and verified here · **PROTOTYPE** = works, low/mid resolution only · **PENDING** = not built yet.

## 1. What is in this folder

| Path | What | Status |
|---|---|---|
| `blend/rewave_pour.blend` | Editable master project (collections, rig, materials, camera, lights, both FLIP domains) | DONE (sims at test/mid res) |
| `scripts/01_build_scene.py` … `07_juice_level.py` | Every step is a re-runnable script (idempotent) — the .blend can be regenerated from the GLB | DONE |
| `scripts/bake_domain.py` | Headless bake: `blender -b rewave_pour.blend -P bake_domain.py -- <domain>` | DONE |
| `web/rewave_pour_rig.json` | Bottle / cap / camera-pan / juice-level tracks, 240 frames, **62 KB (10 KB gzip)** | DONE |
| `web/rewave_pour_player.js` | ES module: ScrollTrigger progress → rig + liquid mesh sequence | DONE (untested in a browser) |
| `web/scrub_test.html` | Standalone test page (site's vendored three.js + GLB) with a scrub slider | DONE (untested in a browser) |
| `web/liquid_frames.*` | Packed liquid mesh sequence | PENDING (needs finished sim) |
| `preview/` | Test stills from low-res sims | PROTOTYPE |
| final-quality bake, Cycles preview video, 6 hero stills | | PENDING |

## 2. Coordinate system (1 Blender unit == 1 Three.js world unit)

* Three `(x, y, z)` → Blender `(x, −z, y)`. Three camera `(0, 0, 7.4)` looking down −Z == Blender camera `(0, −7.4, 0)` looking +Y.
* Camera: perspective, **vertical FOV 30°**, 7.4 units from the bottle plane (`getResponsiveCameraZ()` for h > 800; use 7.6 for h ≤ 800).
  Blender: sensor 24 mm vertical, lens 44.78 mm, 1920×1080 preview.
* Bottle scale 0.038 (`getResponsiveBottleScale()` desktop h > 800), rest position `(0, −0.22, 0)` (= `storyB`).
  Bottle height 2.61 units; neck lip is 1.28 units above the bottle origin.
* Spin about vertical = Blender Z; the pour tilt is a rotation about the **view axis** (Blender Y), top toward screen-right, so the
  label (which faces the camera) stays facing the camera through the whole tilt.

## 3. Master timeline (30 fps, 240 frames = 8.0 s, single continuous timeline)

| Marker | Frame | Event |
|---|---|---|
| M01_Rest | 1 | upright, cap on |
| M02_CapUnscrew_Start | 12 | break-free, rotation ramps up |
| M03_CapDisengaged | 48 | 1.75 turns done, cap leaves the neck (thread lead 3.2 local-units/turn = 0.12 units/turn) |
| M04_CapParked | 84 | cap rests at `(−2.10, 0.10, +1.10)` (three), 1.1 units toward camera → can never touch the swinging bottle (min clearance 0.54) |
| M05_Anticipation | 86 | bottle has dipped −3.5° (weight settle) and holds ≈ 10 frames |
| M06_TiltStart | 96 | accelerating tilt |
| M08_LiquidAtLip | 118 | neck passes horizontal, liquid starts to gather |
| M07_PourAngleReached / M09_StreamRelease | 130 | 118° (+2.5° overshoot, damped) — stream released |
| M10_StreamLandsOnFloor | ≈144 | stream front hits the Formulation surface (provisional) |
| M11_SpreadAcrossFormulation | ≈200 | film spans most of the bottom width (provisional) |
| M12_Settle | 240 | stream closed at f228, surface settling |

Camera pan (= the page scroll): 0 until f140, then eases down to `camY = −6.15` by f192 (floor line sits ≈ 0.6 units above the frame bottom).

## 4. Mapping to ScrollTrigger

`progress = (frame − 1) / 239`. Suggested split of one long pinned timeline: **0 → 0.32** cap opening (Formulation Architecture, `#release`),
**0.32 → 0.55** tilt + release, **0.55 → 0.8** waterfall through Everyday Rhythm (`camY` is the scroll-equivalent offset to apply to the
liquid layer), **0.8 → 1** impact + spread in Formulation. Every channel is a pure function of `progress` ⇒ reversing the scroll reverses
everything with no simulation state.

```js
const pour = new RewavePour({ THREE, scene, productGroup, capMesh: capMeshRoot, juiceMesh: juiceMeshRoot,
                              rigUrl: 'assets/pour/rewave_pour_rig.json', liquidUrl: 'assets/pour/liquid_frames' });
await pour.load();                       // renderer.localClippingEnabled = true  (juice level clipping plane)
ScrollTrigger.create({ trigger: '#release', start: 'top top', end: '+=7000', scrub: true, onUpdate: s => pour.setProgress(s.progress) });
```
The existing cap-lift in the `release-pin` trigger (`capMeshRoot.position.y += 13.5`, 3π) must be removed/replaced — the rig drives the cap now.

## 5. Web delivery — evaluation

| Option | Verdict |
|---|---|
| Morph targets / fixed-topology | ✗ FLIP surfaces change topology every frame; a forced remesh destroys the thin stream and the splash. |
| Vertex-animation texture | ✗ same fixed-topology limitation (and per-vertex normals/tangents are awkward for a refractive surface). |
| **Per-frame quantised mesh sequence** (`06_export_liquid_mesh_seq.py`) | ✔ chosen: 16-bit positions, oct-encoded normals, `u16` indices, random access by frame, gzip. Real transmissive `MeshPhysicalMaterial` in the *same* Three scene as the bottle ⇒ identical camera, correct occlusion, no seams. |
| Transparent image / video sequence | fallback only (alpha + refraction needs a baked backplate; fixed 2-D; large) |

Size is measured on the test sequence and reported in the checkpoint message; it scales with triangle count, so the final bake is decimated to a
triangle budget before packing.

## 6. Open items before sign-off
1. Final-resolution bake (pour domain ≈ 560 cells, spread domain ≈ 560 cells) — several CPU-hours on this machine.
2. Browser verification of `scrub_test.html` (navigation to localhost was refused by the in-app browser in this session).
3. Corridor: the stream lands at x ≈ 2.4–2.7 (right page margin). Confirm against the real Everyday-Rhythm layout on your breakpoints.
4. Cycles preview video + six hero stills from the final cache.
