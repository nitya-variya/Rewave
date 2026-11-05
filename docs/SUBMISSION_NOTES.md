# REWAVE - 3D pour: production notes

## Run
`RUN_REWAVE.bat` (or `python server.py`) and open the printed local address. The page must be served (not opened as a file): the pour player is an ES module and the liquid sequence loads with `fetch`.

## What the 3D sequence does
One scroll-scrubbed (both directions) timeline authored in Blender:
1. **Release** - cap unscrews, bottle pauses, tilts slowly to the right and starts to pour (the liquid gathers at the neck and flows out of the bottle).
2. **Everyday Rhythm** - the same stream keeps falling down the page, behind cards, photos and text.
3. **Formulation (bubbles)** - the waterfall runs through the bubble section and dissolves as the section leaves the screen. No spread / landing effect.

## Files
- `index.html` - journey logic (`updatePourJourney`, `applyPourCameraX`, `syncStageBackgrounds`), drink material, performance layer.
- `assets/pour/rewave_pour_rig.json` - bottle / cap / juice-level tracks (240 frames, 30 fps), 62 KB.
- `assets/pour/rewave_pour_player.js` - maps scroll to the rig and the liquid mesh sequence.
- `assets/pour/liquid_frames.json` + `liquid_frames.bin.gz` - baked FLIP liquid, 9.3 MB, downloaded in idle time (never blocks first paint).
- `blender_pour/` - editable Blender project (`blend/rewave_pour.blend`, scripts 01-07, final cache `cache/pour_full2`). Not part of the deployed site (git-ignored).

## How it fits the existing page
- Section backgrounds (Rituals, Formulation incl. its ambient gradient / floor shade, closing bridge) are painted on `#rw-bgs` planes BEHIND the WebGL canvas; the sections themselves are transparent. Result: the stream is drawn over the background but under every card, text and bubble.
- Narrow screens: the camera slides right while the bottle tilts so the stream stays on screen; the whole pour world scales with the bottle scale.
- Fail-soft: if the liquid files are missing the page works without them.

## Performance
- Removed the 3.6 MB blocking base64 script (`rewave_assets.js`); the GLB / label now load as normal files with `preload` hints.
- Liquid sequence (9.3 MB) downloads in idle time; decoding costs under 1 ms per frame.
- The WebGL canvas only renders when something changes (scroll, pointer, hero animation, playback catching up); idle = no GPU work.
- Adaptive pixel ratio: drops resolution when frames are slow, restores it when there is headroom (capped at 1.5x).
- Liquid playback follows the scroll with critical damping so it never steps.

## Known limits
- The liquid stream is a simulation at 30 fps (topology changes every frame, so it cannot be interpolated). Stream thickness does not taper as much as a real, finer simulation would.
- Tested in an emulated phone / tablet / desktop browser only, not on physical devices.
- Preview video and hero stills were not rendered.

## Removed from the project
Unused files (old archive, `build_index.py` generator, base64 assets, test files) were zipped to `C:\Users\DESK0071\Downloads\REWAVE_unused_backup.zip` and removed from the project folder.
