"""Deterministic five-series development prompt builder, seasons 1–3.

Run: python3 runway_build_v2.py --input episodes.json --output runway_prompts_v2
Builds text prompts and manifests only. It never contacts Runway, spends credits,
generates media, or publishes content. No secret or API credential is needed.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

SERIES = ("momo", "rocket", "yeti", "doodle", "powerpals")
STYLE = {
    "momo": "original soft luminous 3D storybook world; indigo, silver, gold and lavender; rounded silhouettes; bedtime light",
    "rocket": "original rounded 3D toy world; red, yellow and blue construction palette; bright daylight",
    "yeti": "original plush textured 3D characters; gentle pastel colors; warm kitchen lighting",
    "doodle": "original 3D characters in a tactile crayon and paper world; bright mixed colors; warm studio light",
    "powerpals": "original graphic 3D adventure style; saturated hero colors; readable action and expressive faces",
}
SEASON = {1: "foundational story", 2: "phonics and reading", 3: "science, geometry and physics"}
CHARACTER = {
    "momo": "Momo: pearl white glowing round creature, two golden teardrop antennae, amber eyes, crescent belly marking, floats without limbs; Phono: small cream owl librarian with round glasses; Orbit: blue green ringed planet with curious eyes; Twinkle: tiny golden star; Luna: lavender luminous creature",
    "rocket": "Rocket: rounded red mini excavator with yellow stripe, eye windshield, bucket arm and treads; Rivet: small blue silver repair robot with screen face and tool hands; Bitsy: rounded pink drone with one camera eye; Mayor Maple: raccoon with hard hat and vest; Professor Pulley: beaver engineer with goggles and blueprint apron",
    "yeti": "Yum: large soft blue yeti; Num: shorter pink yeti; Tiny: small yellow yeti; Chef Crumb: mouse chef in white apron; Measure Mouse: mouse scientist with glasses and tiny ruler",
    "doodle": "Doodle: multicolor wax crayon creature leaving a colored trail; Melody: teal musical note bird with gold details; Splash: colorful paint blob; Echo: cream folded paper owl; Compass: little golden compass with smiling glass face",
    "powerpals": "Paige: 8 year old girl with curly dark hair and purple gold storybook suit; Max: 9 year old Black boy with glasses and teal orange tech suit; Lina: 8 year old Latina girl with braid and green gold letter suit; Kai: 9 year old Asian boy in red white speed suit; Zoe: 7 year old red haired girl in yellow pink suit. Keep each child recognizable, age appropriate and fully clothed",
}
LOCATIONS = {
    "momo": "Moonbean Meadow at night, silver hills and luminous flowers",
    "rocket": "Tiny Town's colorful construction site in daylight",
    "yeti": "Snack Mountain's pastel kitchen and nearby play area",
    "doodle": "Dreamtopia's paper and crayon sketchbook world",
    "powerpals": "Reader Valley's bright geometry and story powered streets",
}


def validate(episodes: list[dict]) -> None:
    seen = set()
    for ep in episodes:
        key = (ep["series"], ep["season"], ep["number"])
        if key in seen:
            raise ValueError(f"Duplicate episode: {key}")
        seen.add(key)
        if ep["series"] not in SERIES or ep["season"] not in SEASON or not 1 <= ep["number"] <= 15:
            raise ValueError(f"Invalid series/season/episode: {key}")
        if not all(ep.get(k) for k in ("title", "theme", "logline", "beats")) or len(ep["beats"]) < 3:
            raise ValueError(f"Incomplete episode: {key}")
    for series in SERIES:
        for season in (2, 3):
            numbers = {e["number"] for e in episodes if (e["series"], e["season"]) == (series, season)}
            if numbers != set(range(1, 16)):
                raise ValueError(f"Expected episodes 1–15 for {series} season {season}, got {sorted(numbers)}")


def episode_prompts(ep: dict) -> dict[str, str]:
    series = ep["series"]
    identity = f"Reference the approved character sheets. {CHARACTER[series]}. "
    setting = f"{LOCATIONS[series]}. {STYLE[series]}. {SEASON[ep['season']]} theme."
    return {
        "thumbnail": f"Key art for {ep['title']}: {ep['logline']}. One clear focal action and expressive character faces. {identity}{setting} Leave clear space for typography added in post.",
        "opening_keyframe": f"Opening storyboard frame: {ep['beats'][0]}. Wide establishing view, consistent character scale and geography. {identity}{setting}",
        "learning_keyframe": f"Learning moment storyboard frame: {ep['beats'][1]}. Show concrete physical evidence of {ep['theme']}; use a clean overlay in post for exact words, numbers, formulas or labels. {identity}{setting}",
        "closing_keyframe": f"Closing storyboard frame: {ep['beats'][2]}. Resolve the story through a visible action and warm reaction. {identity}{setting}",
    }


def build(episodes: list[dict], output: Path) -> dict:
    validate(episodes)
    output.mkdir(parents=True, exist_ok=True)
    character_lines = [f"[{series}] {CHARACTER[series]}. Turnaround: front, side and back on separate clean views; fixed colors and proportions. {STYLE[series]}" for series in SERIES]
    (output / "01_characters.txt").write_text("\n\n".join(character_lines) + "\n", encoding="utf-8")
    all_lines = []
    prompt_count = 0
    for ep in sorted(episodes, key=lambda e: (e["series"], e["season"], e["number"])):
        prompts = ep.get("image_prompts") or episode_prompts(ep)
        prompt_count += len(prompts)
        lines = [f"=== {ep['series'].upper()} S{ep['season']}E{ep['number']:02d}: {ep['title']} ===", f"THEME: {ep['theme']}", f"LOGLINE: {ep['logline']}", "BEATS:"]
        lines.extend(f"  {i}. {beat}" for i, beat in enumerate(ep["beats"], 1))
        lines.append("IMAGE PROMPTS:")
        lines.extend(f"  [{key}] {prompt}" for key, prompt in prompts.items())
        all_lines.append("\n".join(lines))
    (output / "02_all_episodes.txt").write_text("\n\n".join(all_lines) + "\n", encoding="utf-8")
    for series in SERIES:
        for season in (1, 2, 3):
            subset = [e for e in episodes if e["series"] == series and e["season"] == season]
            if subset:
                header = f"{series.upper()} SEASON {season}: {len(subset)} development episode outlines\n\n"
                entries = [line for ep, line in zip(sorted(episodes, key=lambda e: (e["series"], e["season"], e["number"])), all_lines) if ep in subset]
                (output / f"03_{series}_s{season}.txt").write_text(header + "\n\n".join(entries) + "\n", encoding="utf-8")
    manifest = {"episodes": len(episodes), "image_prompts": prompt_count, "by_season": dict(sorted(Counter(str(e["season"]) for e in episodes).items())), "status": "development prompts; no media generated, scripts or lessons approved", "requires": ["character design lock", "curriculum review", "screenplay and animatic", "human approval", "licensed or owned audio", "platform policy review"]}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("episodes.json"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("runway_prompts_v2"))
    args = parser.parse_args()
    episodes = json.loads(args.input.read_text(encoding="utf-8"))
    print(json.dumps(build(episodes, args.output), indent=2))


if __name__ == "__main__":
    main()
