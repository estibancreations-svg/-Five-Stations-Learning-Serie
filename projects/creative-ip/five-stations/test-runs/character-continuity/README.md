# Character Continuity Calibration — v1

**Run ID:** `character-continuity-calibration-2026-09-28-v1`  
**Mode:** supervised calibration  
**Date:** 2026-09-28  
**Overall status:** `PASS_WITH_HOLDS`

This run contains one controlled still-image scene for each station, generated with the owner-approved character board as the visual reference. The frames test identity, ensemble presence, palette, silhouette, setting, and scene readability before any pilot automation.

| Station | Reference board | Test frame | Controlled scene | Status |
|---|---|---|---|---|
| Momo & the Moonbeans | `assets/character-boards/momo-character-board.png` | `momo-test-run-v1.png` | Momo, Luna, Twinkle, Phono and Orbit investigate a glowing moon rock in Moonbean Meadow. | `verified_with_hold` |
| Rocket & Rivet | `assets/character-boards/rocket-character-board.png` | `rocket-test-run-v1.png` | Rocket, Rivet, Bitsy, Mayor Maple and Professor Pulley test a lever on a model boulder. | `verified_with_hold` |
| Yum Yum Yetis | `assets/character-boards/yeti-character-board.png` | `yeti-test-run-v1.png` | Yum, Num, Tiny, Chef Crumb and Measure Mouse compare ice-cream samples in Snack Mountain Kitchen. | `verified_with_hold` |
| Doodle & the Dreamers | `assets/character-boards/doodle-character-board.png` | `doodle-test-run-v1.png` | Doodle, Melody, Splash, Echo and Compass compare paper airplanes in Dreamtopia. | `verified_with_hold` |
| Power Pals: Code Crew | `assets/character-boards/powerpals-character-board.png` | `powerpals-test-run-v1.png` | Paige, Max, Lina, Kai and Zoe assemble a glowing square geometry gate. | `verified_with_hold` |

## Quality checks

- **Identity and ensemble:** all named characters are present and recognizable against the corresponding board.
- **Continuity:** approved palette, broad silhouette, costume/prop language and station world are retained in the test frame.
- **Exact text / letter lock:** no generated lettering is treated as final. Any letters, formulas, captions or nameplates must be composited and proofread in a later locked pass.
- **Rights and safety:** no new third-party assets or unsafe child-facing action were introduced by this calibration run.
- **Evidence:** the PNG frame, reference board path, manifest record and SHA-256 inventory entry travel together.

## Holds before pilot mode

These are still-image checks, not finished episodes. Motion continuity, turnarounds, shot-to-shot identity, voice, captions, exact text, Runway timing, cost, and final owner sign-off remain untested. Do not mark any character or station `pilot_locked` from this run alone.

The next gate is human visual review of these five frames, followed by a short multi-shot animatic per station. Pilot automation remains disabled until the Assistant Director QC protocol records those approvals.

