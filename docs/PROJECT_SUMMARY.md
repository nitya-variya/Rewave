# REWAVE — Project summary (demo)

## 1. What it is
A single-page marketing site for **REWAVE**, a kiwi-cucumber functional wellness drink. The hero feature is a **scroll-driven 3D bottle sequence**: the real product bottle unscrews its cap, tilts, and pours a simulated liquid stream that keeps flowing down the page through the "Everyday Rhythm" and "Formulation" sections. Scrolling back reverses everything.

Page flow: Hero → Functional by design (matrix) → Release (cap + pour) → Everyday Rhythm → Formulation (physics bubbles) → closing CTA → footer.

## 2. Tech stack
| Layer | Tech |
|---|---|
| 3D rendering | Three.js r160 (WebGL), real product GLB, physical (transmission) materials, studio-style lighting |
| Scroll + animation | GSAP + ScrollTrigger (pinned sections, scrubbing), Lenis (smooth scrolling) |
| Bubbles | Matter.js 2D physics (DOM bubbles inside the Formulation section) |
| Pour authoring | Blender 5.2 — rigging/keyframes (Python), Mantaflow FLIP fluid simulation |
| Pipeline | Python scripts (re-runnable) → JSON rig + quantised mesh sequence → ES-module player |
| Hosting | Static files only (HTML/CSS/JS + assets); no backend |

## 3. How the pour works (end to end)
1. **Model** – the original GLB (cap, shell, juice, label kept as separate meshes) was imported into Blender and rigged with empties/pivots. 1 Blender unit = 1 Three.js unit; camera matches the site (FOV 30°, 7.4 units).
2. **Animation** – one 240-frame / 30 fps master timeline: cap unscrew (thread-lead motion, 1.75 turns), anticipation pause, weighted tilt to the right, pour. Exported as `rewave_pour_rig.json` (bottle, cap, juice-level tracks, 62 KB).
3. **Liquid** – a FLIP simulation (Mantaflow): liquid emitted inside the bottle neck, the bottle shell is a collision object so the stream leaves through the real opening. The baked surface meshes are smoothed, cleaned (air-channel and floating-fragment removal), simplified to ~10k triangles/frame, quantised to 16-bit and packed into `liquid_frames.bin.gz` (9.3 MB, 125 frames) + `liquid_frames.json`.
4. **Playback** – `rewave_pour_player.js` maps scroll position to a frame, applies the rig to the existing bottle nodes (position, rotation, cap, juice-level clipping plane) and swaps the liquid mesh. Playback follows scroll with damping, so it is smooth and reversible (no simulation state at runtime).
5. **Page integration** (`index.html`)
   - Release section is pinned; frames 1–130 play across it (cap, tilt).
   - After the pin the bottle is stuck to the Release section and scrolls away with it; the stream is lengthened so it still hangs from that section to the bottom edge of the bubble section, where the CTA section covers it.
   - Section backgrounds (Rituals, Formulation) are painted on planes **behind** the WebGL canvas, so the liquid shows over the background but under all cards, text and bubbles.
   - The liquid uses the same kiwi-green drink material family as the juice in the bottle.

## 4. Responsive behaviour
- Desktop/laptop: hero bottle is centred in the gap between the two cursive notes (measured from the real outline at every size).
- Portrait tablets and phones use the stacked "phone layout": bottle fitted into the free space above the headline / between heading and card with equal space above and below.
- On narrow screens the camera slides right while the bottle tilts so the stream stays inside the viewport.
- Bubble section keeps large bubbles on tablets and a shorter section height to avoid empty space.

## 5. Performance work
- No blocking base64 script (3.6 MB removed); GLB and label are normal files with preload hints.
- 9.3 MB liquid sequence downloads in idle time; decode < 1 ms per frame.
- WebGL canvas only renders when something changes (scroll, pointer, hero motion, playback catching up).
- Adaptive pixel ratio (max 1.5x) lowers resolution on slow devices and restores it when there is headroom.

## 6. Project folders
- `index.html`, `assets/`, `assets/pour/` — the deployable site.
- `docs/` — this summary, submission notes, integration notes.
- `blender_pour/` — editable Blender project, scripts (01–07), final simulation cache (git-ignored, **do not deploy**).
- `REWAVE_unused_backup.zip` (in Downloads) — files removed during clean-up.

## 7. Known limits
- The stream is a 30 fps simulation (topology changes each frame, so it cannot be interpolated) and does not thin out as much as a finer, much slower simulation would.
- Tested in an emulated browser (desktop, laptop, tablet, phone); real-device testing is still required.
- Preview video and hero stills were not rendered.
