# Five Stations: Seasons 2 and 3 development package

This package translates the supplied expansion into **150 indexed episode concepts** (five series × two seasons × fifteen episodes), a repeatable image prompt builder, and a gated production plan. Season 1 was described but no Season 1 episode source was supplied or found in this repository. The builder accepts Season 1 entries when added to `episodes.json`; the current catalog does not claim 225 completed episodes. No images, animation, finished scripts, audio, or videos are included.

## Build

```bash
cd projects/creative-ip/five-stations
python3 build_catalog.py
python3 runway_build_v2.py --input episodes.json --output runway_prompts_v2
```

`episode_source.py` is the editable editorial input. `episodes.json` is its machine-readable export. The builder writes a character prompt file, an all-episodes prompt file, ten individual series/season files, and a manifest. Each episode has four distinct image prompts (thumbnail, opening, teaching, closing), yielding **600 development prompts** for Seasons 2 and 3. These are text instructions only. Re-run the builder after editing source; no API call, upload, media generation, or publication occurs.

## Editorial specification

| Series | Core setting | New science or literacy guide | On-screen age approach |
| --- | --- | --- | --- |
| Momo & the Moonbeans | Moonbean Meadow | Phono, Orbit | gentle, quiet inquiry |
| Rocket & Rivet | Tiny Town | Professor Pulley | build, test and fix |
| Yum Yum Yetis | Snack Mountain | Measure Mouse | food and sensory experiments |
| Doodle & the Dreamers | Dreamtopia | Compass | draw, compare and record |
| Power Pals: Code Crew | Reader Valley | existing team | cooperative problem solving |

Lock each character only after an original turnaround, palette, voice, expressions, gestures, and silhouette are approved. A text description alone cannot lock visual identity. Store approved references and use them for every shot; record a shot ID, input reference hash, model/version, output asset ID and continuity review. The original upload names an existing animation studio in every style suffix; this version describes original visual traits instead of directing imitation.

Every episode needs a story question, prior knowledge, one observable test or reading demonstration, a wrong-but-plausible guess, evidence that changes the characters' minds, a retell, and an optional extension. The learning action must occupy real screen time. For literacy, build exact letters and words in compositing with a proofread overlay; image generators may misspell or distort type. For science, separate fantasy premise from factual explanation; show what was observed and avoid universal conclusions from one test.

## Reviewable production state machine

`idea → curriculum review → screenplay → storyboard and references → approved animatic → shot generation → voice/music/edit → factual/accessibility review → owner approval → upload → post-release QA`

Create one record per episode with series, season, episode number, grade band, learning objective, curriculum source, characters, setting, script revision, concept review, reference hashes, shot list, asset IDs, generation costs, audio rights, caption status, accessibility check, scientific review, owner approval, publish status, platform ID, and audit timestamps. An agent may draft the next stage automatically; transitions to paid generation and publication require the owner's configured approval. Preserve rejected versions and reviewer notes. Queue failed jobs for retry with a bounded attempt count; never report a completed episode because a prompt file exists.

For each approved scene, make consistent start/end keyframes; animate shots with current supported media models, inspect motion and continuity, record the usable seconds, stitch the edit, mix licensed audio, add accurate captions, and review the whole program on phone and TV. Prompt files are **not** a Runway API integration. Authentication, API model selection, duration constraints, asset uploads, task polling, retry handling, cost controls, and storage must be implemented against current API documentation when generation is approved.

## Editorial corrections required before production

- **Momo S2E3:** CAT blends /k/ /ă/ /t/; those letters do not spell *meow*. The cat's voice returning is fictional story resolution, not a phonics causal claim.
- **Yeti S2E5:** *Éclair* does not demonstrate the English final-e rule; the source now uses CAN → CANE. A later rewrite should choose food-connected words naturally.
- **Rocket S3E2 and S3E6:** Levers and ramps can trade distance for reduced force; neither produces extra energy. A fixed pulley changes the direction of force; it does not automatically make lifting require less force.
- **Momo S3E6 / Yeti S3E3:** Sinking and floating require a buoyancy lesson with shape and displaced water, not a single word definition of density.
- **Momo S3E10 / Yeti S3E8:** A magnet attracts certain materials; repulsion is demonstrated with two magnets, not a magnet and arbitrary metal.
- **Rocket S3E13 / Power Pals S3E4:** Speed is distance over time; velocity also includes direction.
- **Yeti S3E12:** Vinegar and baking soda can make a demonstration fizz, but a cake's rise is a separate controlled food experiment with appropriate leavening.
- **Doodle S3E7:** A golden ratio pattern is a particular mathematical construction, not an automatic property of every natural spiral.
- **Power Pals S3E5:** Use safe sound experiments instead of a weapon demonstration. For ages 5–8, keep plots cooperative and any peril mild.

The supplied 30 screenplay sample claim is not supported by the uploaded text: it contains **five excerpts**, one per series. These remain reference material for the screenplay stage and need individual editorial review. Likewise, price bands and claims of licensing eligibility are commercial hypotheses, not sales or accreditation evidence. School licensing requires independently reviewed curriculum alignment, accessibility, rights, procurement requirements, and pilot outcomes.

## Schedule math and platform decision

The supplied weekday grid publishes **five videos per day × five days = 25 per week**, or five per channel per week. If there are 225 episodes after Season 1 is actually supplied, that inventory lasts **nine weeks** at the grid's pace. At two uploads per channel per week, inventory lasts **22.5 weeks** across five channels. To sustain 4.5 years at two per channel weekly would take about **2,340 episodes**. Use a pilot cadence of up to two approved videos per channel weekly only after the episode pipeline meets quality and cost gates.

Set the audience truthfully as Made for Kids where the intended audience is children. There is no verified automatic “Learning” tag entitlement, placement guarantee, or educational licensing status from having phonics and STEM episodes. YouTube Kids eligibility and recommendation depend on its current policies and quality review. Keep product promotion out of the children's narrative and route any adult commerce to an adult-directed site; have platform counsel review the actual channel and linked experiences before launch.

## Release gates

1. Approve age band for each series (the five series range from bedtime to early elementary), and verify each lesson against a curriculum specialist.
2. Approve original character design sheets, voices, and a pilot script per series.
3. Create two tested episode animatics, with exact on-screen literacy overlays and documented science corrections.
4. Budget and generate only approved shots; record actual cost, usable footage, and review outcomes.
5. Publish a small pilot after captions, audio rights, platform audience settings, and owner approval; learn from comprehension and retention data before scaling.

## Sources for operational checks

- [Runway Gen-4 image prompting](https://help.runwayml.com/hc/en-us/articles/35694045317139-Gen-4-Image-Prompting-Guide) (positive prompts; negative phrasing can be counterproductive).
- [Runway image-to-video prompting](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide).
- [YouTube Kids content policies](https://support.google.com/youtube/answer/10938174).
- [YouTube kids and family quality principles](https://support.google.com/youtube/answer/10774223).
- [YouTube Made for Kids FAQ](https://support.google.com/youtube/answer/9684541).
