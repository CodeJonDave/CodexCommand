#!/usr/bin/env python3

from pathlib import Path
import math

OUT = Path.home() / "Projects/CodexCommand/Assets/crest/source/FCV_CC01_Crest_Master.svg"

CX = 1024
CY = 1024

OUTER_RING_RADIUS = 880
OUTER_RING_WIDTH = 118

BLUE_RING_RADIUS = 790
BLUE_RING_WIDTH = 10

BLACK_RING_RADIUS = 665.6
BLACK_RING_WIDTH = 16

def polar(radius: float, degrees: float) -> tuple[float, float]:
    angle = math.radians(degrees - 90)
    return (
        CX + radius * math.cos(angle),
        CY + radius * math.sin(angle),
    )


def curved_letters(
    text: str,
    radius: float,
    center_degrees: float,
    span_degrees: float,
    font_size: int,
    color: str,
    rotate_offset: float = 0,
    reverse_text: bool = False,
) -> str:
    chars = list(text[::-1] if reverse_text else text)
    start = center_degrees - span_degrees / 2
    step = span_degrees / max(len(chars) - 1, 1)

    output = []
    for index, char in enumerate(chars):
        degree = start + index * step
        x, y = polar(radius, degree)
        rotation = degree + rotate_offset

        if rotation > 180:
            rotation -= 360
        if rotation < -180:
            rotation += 360

        output.append(
            f'<text x="{x:.2f}" y="{y:.2f}" '
            f'text-anchor="middle" dominant-baseline="middle" '
            f'fill="{color}" font-family="Cascadia Code, monospace" '
            f'font-size="{font_size}" font-weight="800" '
            f'transform="rotate({rotation:.2f} {x:.2f} {y:.2f})">{char}</text>'
        )

    return "\n".join(output)


ticks = []
for degree in range(0, 360, 5):
    major = degree % 30 == 0
    inner_radius = 690 if major else 715
    outer_radius = 755
    x1, y1 = polar(inner_radius, degree)
    x2, y2 = polar(outer_radius, degree)

    ticks.append(
        f'<line x1="{x1:.2f}" y1="{y1:.2f}" '
        f'x2="{x2:.2f}" y2="{y2:.2f}" '
        f'stroke="#101820" stroke-width="{7 if major else 3}"/>'
    )


degree_labels = []
for degree in range(0, 360, 30):
    x, y = polar(782, degree)
    degree_labels.append(
        f'<text x="{x:.2f}" y="{y:.2f}" '
        f'text-anchor="middle" dominant-baseline="middle" '
        f'fill="#101820" font-family="Cascadia Code, monospace" '
        f'font-size="34" font-weight="700">{degree}°</text>'
    )


cardinals = []
for label, degree in {"N": 0, "E": 90, "S": 180, "W": 270}.items():
    x, y = polar(575, degree)
    color = "#A00000" if label == "N" else "#4F6B3C"

    cardinals.append(
        f'<text x="{x:.2f}" y="{y:.2f}" '
        f'text-anchor="middle" dominant-baseline="middle" '
        f'fill="{color}" font-family="Cascadia Code, monospace" '
        f'font-size="76" font-weight="900">{label}</text>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="2048" height="2048" viewBox="0 0 2048 2048">
  <rect width="2048" height="2048" fill="none"/>

  <circle cx="1024" cy="1024" r="{OUTER_RING_RADIUS}" fill="none" stroke="#4F6B3C" stroke-width="{OUTER_RING_WIDTH}"/>
  <circle cx="1024" cy="1024" r="{BLUE_RING_RADIUS}" fill="none" stroke="#4682B4" stroke-width="{BLUE_RING_WIDTH}"/>
  <circle cx="1024" cy="1024" r="{BLACK_RING_RADIUS}" fill="none" stroke="#101820" stroke-width="{BLACK_RING_WIDTH}"/>

  <g id="outer-ring-text">
    {curved_letters("FCV • CC-01", 875, 0, 58, 72, "#D8DEE9")}
    {curved_letters("CODEX", 875, 270, 44, 72, "#D8DEE9")}
    {curved_letters("COMMAND", 875, 90, 48, 72, "#D8DEE9")}
    {curved_letters("ERULIAF TON SI GNIKAERB", 875, 180, 88, 72, "#D8DEE9", rotate_offset=180)}
  </g>

  <g id="degree-ticks">
    {"".join(ticks)}
  </g>

  <g id="degree-labels">
    {"".join(degree_labels)}
  </g>

  <g id="cardinal-labels">
    {"".join(cardinals)}
  </g>

  <g id="split-vector-compass">
    <polygon points="1024,505 972,835 1024,780 1076,835" fill="#A00000"/>
    <polygon points="1543,1024 1213,972 1268,1024 1213,1076" fill="#4F6B3C"/>
    <polygon points="1024,1543 972,1213 1024,1268 1076,1213" fill="#4F6B3C"/>
    <polygon points="505,1024 835,972 780,1024 835,1076" fill="#4F6B3C"/>
  </g>

  <circle cx="1024" cy="1024" r="102.4" fill="#101418" stroke="#C7922A" stroke-width="24"/>
  <circle cx="1024" cy="1024" r="28" fill="#D8DEE9"/>
</svg>
'''

OUT.write_text(svg)
print(f"Created {OUT}")
