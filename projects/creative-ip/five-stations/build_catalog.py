"""Convert the editorial source into the schema consumed by runway_build_v2.py."""
import json
from pathlib import Path

from episode_source import EPISODES
from runway_build_v2 import validate


def main() -> None:
    episodes = []
    for (series, season), block in EPISODES.items():
        for number, line in enumerate(block.splitlines(), 1):
            title, theme, story = [part.strip() for part in line.split("|", 2)]
            moments = [part.strip() for part in story.split(";")]
            beats = [f"The problem emerges: {moments[0]}", f"The friends investigate {theme}: {moments[1] if len(moments) > 1 else moments[0]}", f"They apply the idea, observe the result and retell what changed: {moments[-1]}"]
            episodes.append({"series": series, "season": season, "number": number, "title": title, "theme": theme, "logline": story[0].upper() + story[1:] + ".", "beats": beats})
    validate(episodes)
    destination = Path(__file__).with_name("episodes.json")
    destination.write_text(json.dumps(episodes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(episodes)} episodes to {destination}")


if __name__ == "__main__":
    main()
