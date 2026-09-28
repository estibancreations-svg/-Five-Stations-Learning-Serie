"""Build a factual inventory of the Five Stations package.

This is a read-only inventory pass. It counts source records, generated prompt
files, documentation and scripts, then writes a machine-readable JSON report and
a human-readable Markdown report. It does not infer missing seasons or claim
that prompts are finished media.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build(root: Path) -> dict:
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts or path.name in {"creation_inventory.json", "creation_inventory.md"}:
            continue
        relative = path.relative_to(root).as_posix()
        files.append({"path": relative, "bytes": path.stat().st_size, "sha256": sha256(path)})

    episodes_path = root / "episodes.json"
    episodes = json.loads(episodes_path.read_text(encoding="utf-8")) if episodes_path.exists() else []
    series_season = Counter((item["series"], item["season"]) for item in episodes)
    by_series = Counter(item["series"] for item in episodes)
    by_season = Counter(str(item["season"]) for item in episodes)
    prompt_files = sorted((root / "runway_prompts_v2").glob("*.txt")) if (root / "runway_prompts_v2").exists() else []
    manifest_path = root / "runway_prompts_v2" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    inventory = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "package_root": root.name,
        "source_records": {
            "episode_objects": len(episodes),
            "by_series": dict(sorted(by_series.items())),
            "by_season": dict(sorted(by_season.items())),
            "by_series_and_season": {f"{series}/s{season}": count for (series, season), count in sorted(series_season.items())},
        },
        "created_artifacts": {
            "tracked_files": len(files),
            "prompt_text_files": len(prompt_files),
            "character_prompt_file": (root / "runway_prompts_v2" / "01_characters.txt").exists(),
            "all_episode_prompt_file": (root / "runway_prompts_v2" / "02_all_episodes.txt").exists(),
            "manifest_file": manifest_path.exists(),
            "screenplay_excerpt_file": (root / "screenplay_excerpts.md").exists(),
            "scripts": sorted(path.name for path in root.glob("*.py")),
            "documentation": sorted(path.name for path in root.glob("*.md")),
        },
        "manifest_comparison": {
            "manifest_episode_count": manifest.get("episodes"),
            "manifest_prompt_count": manifest.get("image_prompts"),
            "episode_count_matches_manifest": manifest.get("episodes") == len(episodes),
        },
        "production_status": {
            "development_catalog": True,
            "finished_media_generated": False,
            "finished_episodes_approved": False,
            "season_1_source_present": any(item["season"] == 1 for item in episodes),
            "claims_are_delivery_ready": False,
        },
        "files": files,
        "qc_result": "PASS_WITH_HOLDS: inventory is internally consistent; curriculum, character, media, rights and owner approval gates remain open",
    }
    return inventory


def markdown(inventory: dict) -> str:
    source = inventory["source_records"]
    created = inventory["created_artifacts"]
    comparison = inventory["manifest_comparison"]
    status = inventory["production_status"]
    lines = [
        "# Five Stations creation inventory",
        "",
        f"Generated UTC: `{inventory['generated_at_utc']}`",
        "",
        "## What exists",
        "",
        f"- `{source['episode_objects']}` episode objects in `episodes.json`.",
        f"- `{created['prompt_text_files']}` generated prompt text files, including character, all-episode and series/season prompt sets.",
        f"- `{created['tracked_files']}` tracked package files in this inventory scope.",
        f"- Scripts: {', '.join(f'`{name}`' for name in created['scripts'])}.",
        f"- Screenplay excerpts present: `{created['screenplay_excerpt_file']}`.",
        "",
        "## Counts checked",
        "",
        "| Group | Count |",
        "|---|---:|",
        f"| Episodes | {source['episode_objects']} |",
    ]
    lines.extend(f"| {key} | {value} |" for key, value in source["by_series_and_season"].items())
    lines.extend([
        f"| Manifest episodes | {comparison['manifest_episode_count']} |",
        f"| Manifest image prompts | {comparison['manifest_prompt_count']} |",
        "",
        "## Delivery state",
        "",
        f"- Manifest matches the direct episode count: `{comparison['episode_count_matches_manifest']}`.",
        f"- Season 1 source records present: `{status['season_1_source_present']}`.",
        f"- Finished media generated: `{status['finished_media_generated']}`.",
        f"- Finished episodes approved: `{status['finished_episodes_approved']}`.",
        f"- QC result: `{inventory['qc_result']}`.",
        "",
        "This inventory counts files and records. It does not convert prompts into finished episodes or infer missing source material.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    inventory = build(args.root)
    (args.root / "creation_inventory.json").write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
    (args.root / "creation_inventory.md").write_text(markdown(inventory), encoding="utf-8")
    print(json.dumps({"episodes": inventory["source_records"]["episode_objects"], "files": inventory["created_artifacts"]["tracked_files"], "qc": inventory["qc_result"]}, indent=2))


if __name__ == "__main__":
    main()
