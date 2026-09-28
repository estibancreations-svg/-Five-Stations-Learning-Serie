# Character board, lettering and pilot-mode lock

## Purpose

The character boards in `assets/character-boards/` are visual reference candidates for the five stations. They are the first-run anchors used to reduce identity drift when scenes move between VisionWeaver, Runway, image systems, video systems, compositing, editing and voice production.

They are **v1 reference candidates**, not final approval. The empty nameplates are intentional: exact names and lesson text are added in a controlled post-production layer. Image generation is not a reliable source for spelling, labels, phonics, formulas or scientific notation.

## Board order lock

The panel order is fixed and must never change without a revision record:

| Board | Panel 1 | Panel 2 | Panel 3 | Panel 4 | Panel 5 |
|---|---|---|---|---|---|
| Momo | Momo | Luna | Twinkle | Phono | Orbit |
| Rocket | Rocket | Rivet | Bitsy | Mayor Maple | Professor Pulley |
| Yeti | Yum | Num | Tiny | Chef Crumb | Measure Mouse |
| Doodle | Doodle | Melody | Splash | Echo | Compass |
| Power Pals | Paige | Max | Lina | Kai | Zoe |

## Lock record for every character

Each approved character needs:

`character_id · board_revision · panel_index · reference_asset_hash · silhouette_notes · palette · scale · expression range · voice_id · allowed props · prohibited changes · reviewer · approval timestamp`

Downstream systems receive the reference asset and lock record as inputs. They do not recreate the character from a loose paragraph when an approved reference exists. A scene fails continuity review if the character changes species, age, body plan, panel identity, palette, wardrobe, prop identity or silhouette without an approved revision.

## First run

The first run is a supervised calibration run. For each station:

1. Approve the board and its panel order.
2. Generate a neutral turnaround and one expression sheet per character.
3. Generate one test scene with the full cast and one test scene with a single character.
4. Compare outputs against the board using identity, scale, palette, prop and setting checks.
5. Record every correction in the Q&A log.
6. Freeze the accepted references, prompt fragments, seed or model settings where available, and asset hashes.

The system enters pilot mode only after the first run has a signed review and no unresolved identity blocker.

## Pilot mode

Pilot mode may automate intake, scene breakdown, prompt assembly, reference attachment, generation queueing, polling, caption draft, voice draft and report assembly. It must pause for configured gates:

- new character or character revision;
- new location or major prop;
- any text that must be exact;
- a scientific or literacy claim;
- a failed continuity score;
- an audio rights or voice identity mismatch;
- a cost, safety or platform hold;
- final owner approval.

Pilot mode learns from approved Q&A records and rejected outputs. It may reuse an answer with matching project, character, lesson, model and revision context. It must ask again when the context or evidence differs.

## Handoff to another creative system

The handoff package contains the approved board, board order table, character lock records, scene references, exact prompt fragments, letter lock, voice map, Q&A log, rejection examples and delivery status. The receiving system must confirm it loaded the package before generating. Its output is accepted only after the same lock checks pass.

## Voiceover handoff

ElevenLabs may produce voiceover after the script, pronunciation guide and voice ID are approved. The package must include:

- exact approved narration;
- pronunciation guide for names, phonemes and technical terms;
- voice ID and approved voice revision;
- pacing, emphasis and pause notes;
- language and caption transcript;
- audio file hash and rights record.

ElevenLabs output is an asset under review. It does not determine the canonical script, lesson wording or character identity.
