# Three-Shot Continuity Test — v1

**Run ID:** `three-shot-continuity-2026-09-29-v1`  
**Mode:** supervised reference-conditioned generation  
**Overall status:** `PASS_WITH_HOLDS`  
**Pilot mode:** not enabled

This gate tests each station across an opening, action, and closing frame using the owner-approved character board as the reference. It is designed to expose identity drift, palette drift, prop drift, and setting drift before animation.

| Station | Frames | Result | Review note |
|---|---|---|---|
| Momo & the Moonbeans | `momo/01-opening.png` → `02-action.png` → `03-closing.png` | `provisional_pass` | Five-character ensemble and Moonbean palette persist; exact text remains locked out. |
| Rocket & Rivet | `rocket/01-opening.png` → `02-action.png` → `03-closing.png` | `provisional_pass` | Construction setting, five-character ensemble and lever prop persist; motion has not been tested. |
| Yum Yum Yetis | `yeti/01-opening.png` → `02-action.png` → `03-closing.png` | `provisional_pass` | Plush identities, kitchen setting and food props persist; generated food details are not final lesson evidence. |
| Doodle & the Dreamers | `doodle/01-opening.png` → `02-action.png` → `03-closing.png` | `provisional_pass` | Crayon/origami world and five-character ensemble persist; paper-plane motion is still-image only. |
| Power Pals: Code Crew | `powerpals/01-opening.png` → `02-action.png` → `03-closing.png` | `provisional_pass` | Five hero identities, suits and geometry setting persist; generated shapes are visual placeholders, not final lettering. |

## Checks completed

- Three frames were generated per station from the approved board reference.
- Opening/action/closing compositions preserve the intended ensemble and world.
- No generated lettering, captions, formulas, or nameplates are accepted as final; the Letter Lock compositor remains authoritative.
- The images are calibration evidence, not finished episode media.

## Holds before pilot lock

Human owner review is still required. Turnarounds, image-to-video motion, shot-to-shot identity during animation, voiceover, captions, exact-text compositing, cost, and final delivery QC remain open. Any failed review becomes a targeted regeneration rather than a silent substitution.

