"""Score persistence for NetSim."""

from __future__ import annotations

import json
from pathlib import Path


def load_scores(path: Path) -> dict[str, int]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(data, dict):
        return {}
    scores: dict[str, int] = {}
    for key, value in data.items():
        if isinstance(key, str) and isinstance(value, int):
            scores[key] = max(0, min(100, value))
    return scores


def save_scores(path: Path, scores: dict[str, int]) -> None:
    path.write_text(json.dumps(scores, indent=2, sort_keys=True) + "\n")
