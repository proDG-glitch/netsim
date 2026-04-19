"""Banner rendering helpers."""

from __future__ import annotations

from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from netsim.data.text_content import FONT, LESSONS_ASCII_HEADER, NETSIM_ASCII_HEADER


def pixel_text(label: str, style: str = "#b8e4ff bold") -> Text:
    rows = ["", "", "", "", ""]
    for char in label.upper():
        glyph = FONT.get(char, FONT[" "])
        for idx, part in enumerate(glyph):
            rows[idx] += f"{part}  "
    return Text("\n".join(rows), style=style)


def render_banner(label: str):
    banner = (
        Text(NETSIM_ASCII_HEADER, style="#b8e4ff bold")
        if label.upper() == "NETSIM"
        else Text(LESSONS_ASCII_HEADER, style="#b8e4ff bold")
        if label.upper() == "LESSONS"
        else Text(label, style="#b8e4ff bold")
        if "\n" in label
        else pixel_text(label)
    )
    return Panel(
        Align.center(banner, vertical="middle"),
        border_style="#53b4ff",
        padding=(1, 2),
    )
