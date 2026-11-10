#!/usr/bin/env python3
"""Regenerate the profile artwork with Python 3.9 or newer."""

# PALETTE CONFIGURATION
# Change this name, then run: python generate_assets.py
# Options: paper, porcelain, iris, moss, petrol, ultramarine,
#          apricot, vermilion, glacier, amber.
ACTIVE_PALETTE = "paper"

# Edit the light and dark hex colors below to customize a palette.
# bg/surface are backgrounds, fg is text, muted is secondary text,
# accent is the highlight, tint is the soft fill, on_accent is text on accent.
PALETTES = {
    "paper": {
        "light": {
            "bg": "#FAF4EB",
            "surface": "#FFF9F2",
            "fg": "#2C211D",
            "muted": "#674E42",
            "accent": "#9C3037",
            "tint": "#F5E1D8",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#1D1716",
            "surface": "#2A2120",
            "fg": "#F7ECE4",
            "muted": "#CBB1A5",
            "accent": "#F4A1A5",
            "tint": "#482C30",
            "on_accent": "#1D1716",
        },
    },
    "porcelain": {
        "light": {
            "bg": "#F8F9FC",
            "surface": "#FFFFFF",
            "fg": "#151923",
            "muted": "#4D5869",
            "accent": "#2454CC",
            "tint": "#E7EEFF",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#121620",
            "surface": "#1A202B",
            "fg": "#F0F4FC",
            "muted": "#AEBAD0",
            "accent": "#91ACFF",
            "tint": "#233255",
            "on_accent": "#121620",
        },
    },
    "iris": {
        "light": {
            "bg": "#F7F6FC",
            "surface": "#FFFFFF",
            "fg": "#211C36",
            "muted": "#584D72",
            "accent": "#5841B9",
            "tint": "#EBE6FF",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#15131D",
            "surface": "#201D2C",
            "fg": "#F2EEFF",
            "muted": "#BEB3D5",
            "accent": "#B9A8FF",
            "tint": "#352C57",
            "on_accent": "#15131D",
        },
    },
    "moss": {
        "light": {
            "bg": "#F7F5EA",
            "surface": "#FFFCF3",
            "fg": "#262C22",
            "muted": "#505D46",
            "accent": "#455B2C",
            "tint": "#E9EEDB",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#161C15",
            "surface": "#242D21",
            "fg": "#F0F0DF",
            "muted": "#BFC8AE",
            "accent": "#BBD58B",
            "tint": "#303E27",
            "on_accent": "#161C15",
        },
    },
    "petrol": {
        "light": {
            "bg": "#F4F3EE",
            "surface": "#FDFDF9",
            "fg": "#152B2B",
            "muted": "#425B59",
            "accent": "#116761",
            "tint": "#D9EAE6",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#10201F",
            "surface": "#1A302E",
            "fg": "#E8F3F1",
            "muted": "#ABC9C1",
            "accent": "#82D8C7",
            "tint": "#23413D",
            "on_accent": "#10201F",
        },
    },
    "ultramarine": {
        "light": {
            "bg": "#FAF5E9",
            "surface": "#FFFAF0",
            "fg": "#1F2736",
            "muted": "#555D66",
            "accent": "#143FCC",
            "tint": "#E2EBFD",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#151D30",
            "surface": "#1F2C45",
            "fg": "#F0F3FA",
            "muted": "#B6C2D9",
            "accent": "#9AB5FF",
            "tint": "#2C4069",
            "on_accent": "#151D30",
        },
    },
    "apricot": {
        "light": {
            "bg": "#FFF4EC",
            "surface": "#FFF9F6",
            "fg": "#321C32",
            "muted": "#674A60",
            "accent": "#873D68",
            "tint": "#F5D9E7",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#221621",
            "surface": "#31232E",
            "fg": "#F7EEF5",
            "muted": "#D9B8CE",
            "accent": "#F3AEC9",
            "tint": "#513349",
            "on_accent": "#221621",
        },
    },
    "vermilion": {
        "light": {
            "bg": "#F8F7F4",
            "surface": "#FFFFFF",
            "fg": "#252323",
            "muted": "#5D5554",
            "accent": "#A83629",
            "tint": "#FDE4DC",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#1C1818",
            "surface": "#292223",
            "fg": "#FFF1EC",
            "muted": "#D6B8AF",
            "accent": "#FF9B88",
            "tint": "#4E2D2A",
            "on_accent": "#1C1818",
        },
    },
    "glacier": {
        "light": {
            "bg": "#F1F7FA",
            "surface": "#F8FCFF",
            "fg": "#1D313B",
            "muted": "#465E6B",
            "accent": "#A2384F",
            "tint": "#F7E1E8",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#14232C",
            "surface": "#1D3340",
            "fg": "#EDF6FB",
            "muted": "#ACC9D8",
            "accent": "#FFA8BB",
            "tint": "#442B3D",
            "on_accent": "#14232C",
        },
    },
    "amber": {
        "light": {
            "bg": "#F5F3EF",
            "surface": "#FCFAF6",
            "fg": "#25242E",
            "muted": "#5D5860",
            "accent": "#875211",
            "tint": "#F0E3C8",
            "on_accent": "#FFFFFF",
        },
        "dark": {
            "bg": "#151B24",
            "surface": "#1E2935",
            "fg": "#F6F1E7",
            "muted": "#C9BFB0",
            "accent": "#F5BF6D",
            "tint": "#3E3226",
            "on_accent": "#151B24",
        },
    },
}

from pathlib import Path
import re


# SVG artwork templates follow. Braced names refer to colors configured above.
ARTWORK = {
    "nameplate": """
<svg role="img" aria-label="Sarthak Rathi" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 160" preserveAspectRatio="xMidYMid meet" width="720" height="160">
  <title>Sarthak Rathi</title>
  <rect width="720" height="160" fill="{bg}" rx="3"/>
  <path d="M26 132H694" fill="none" stroke="{accent}" stroke-width="2"/>
  <text x="25" y="104" fill="{fg}" font-family="Georgia, 'Times New Roman', serif" font-size="80" letter-spacing="-4">Sarthak Rathi<tspan fill="{accent}">.</tspan></text>
  <circle cx="668" cy="43" r="10" fill="{accent}"/>
  <circle cx="691" cy="43" r="4" fill="{muted}"/>
</svg>
""",
    "ifkg": """
<svg role="img" aria-label="Food Knowledge Graph. RDF and a tilted GraphQL block over a network of graph nodes." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 270" width="340" height="270">
  <title>Food Knowledge Graph. RDF and a tilted GraphQL block over a network of graph nodes.</title>
  <rect width="340" height="270" fill="{bg}"/>
  <g fill="none" stroke="{muted}" stroke-width="1.5" opacity=".45">
    <path d="M49 53L149 33L281 64L292 198L195 235L63 219L49 53M49 53L168 128L281 64M149 33L168 128L63 219M168 128L195 235M168 128L292 198"/>
  </g>
  <g fill="{tint}" stroke="{accent}" stroke-width="1.5">
    <circle cx="49" cy="53" r="8"/>
    <circle cx="149" cy="33" r="10"/>
    <circle cx="281" cy="64" r="9"/>
    <circle cx="292" cy="198" r="8"/>
    <circle cx="195" cy="235" r="10"/>
    <circle cx="63" cy="219" r="9"/>
    <circle cx="168" cy="128" r="11"/>
  </g>
  <g font-family="ui-monospace, SFMono-Regular, Consolas, monospace" font-weight="600" text-anchor="middle" font-size="32" fill="{accent}">
    <rect x="24" y="78" width="111" height="66" rx="5" fill="{surface}" stroke="{accent}" stroke-width="1.5"/>
    <text x="79.5" y="122">RDF</text>
    <g transform="rotate(-4 212 155)">
      <rect x="115" y="120" width="194" height="70" rx="5" fill="{surface}" stroke="{accent}" stroke-width="1.5"/>
      <text x="212" y="166">GraphQL</text>
    </g>
  </g>
</svg>
""",
    "yelp": """
<svg role="img" aria-label="Yelp evaluation. Prediction error examined separately across vote ranges." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 112" width="340" height="112">
  <title>Yelp evaluation. Prediction error examined separately across vote ranges.</title>
  <rect width="340" height="112" fill="{bg}"/>
  <g font-family="ui-monospace, Consolas, monospace" text-anchor="middle" font-size="16" fill="{fg}">
    <rect x="18" y="25" width="66" height="58" rx="4" fill="{tint}"/>
    <rect x="97" y="25" width="66" height="58" rx="4" fill="{tint}"/>
    <rect x="176" y="25" width="66" height="58" rx="4" fill="{tint}"/>
    <rect x="255" y="25" width="66" height="58" rx="4" fill="{accent}"/>
    <text x="51" y="60">0</text>
    <text x="130" y="60">1–5</text>
    <text x="209" y="60">6–20</text>
    <text x="288" y="60" fill="{on_accent}">21+</text>
  </g>
</svg>
""",
    "word-games": """
<svg role="img" aria-label="Word Games in Rust. A five-letter word represented as letter tiles." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 112" width="340" height="112">
  <title>Word Games in Rust. A five-letter word represented as letter tiles.</title>
  <rect width="340" height="112" fill="{bg}"/>
  <g font-family="ui-monospace, Consolas, monospace" font-size="27" text-anchor="middle">
    <g fill="{tint}">
      <rect x="25" y="29" width="50" height="54" rx="3"/>
      <rect x="85" y="29" width="50" height="54" rx="3"/>
      <rect x="145" y="29" width="50" height="54" rx="3"/>
      <rect x="205" y="29" width="50" height="54" rx="3"/>
    </g>
    <rect x="265" y="29" width="50" height="54" rx="3" fill="{accent}"/>
    <g fill="{fg}">
      <text x="50" y="65">W</text>
      <text x="110" y="65">O</text>
      <text x="170" y="65">R</text>
      <text x="230" y="65">D</text>
    </g>
    <text x="290" y="65" fill="{on_accent}">S</text>
  </g>
</svg>
""",
    "indisight": """
<svg role="img" aria-label="IndiSight. District data, SQL retrieval, policy documents, and a benchmark contract." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 118" width="700" height="118">
  <title>IndiSight. District data, SQL retrieval, policy documents, and a benchmark contract.</title>
  <rect width="700" height="118" fill="{bg}"/>
  <path d="M163 59H239M391 59H468" stroke="{muted}" stroke-width="2" fill="none"/>
  <g font-family="ui-monospace, Consolas, monospace" text-anchor="middle" font-size="17">
    <rect x="20" y="29" width="143" height="60" rx="4" fill="{tint}"/>
    <text x="91.5" y="66" fill="{fg}">DISTRICT DATA</text>
    <rect x="239" y="29" width="152" height="60" rx="4" fill="{tint}"/>
    <text x="315" y="66" fill="{fg}">SQL + POLICY</text>
    <rect x="468" y="29" width="212" height="60" rx="4" fill="{accent}"/>
    <text x="574" y="66" fill="{on_accent}">ARTIFACT CONTRACT</text>
  </g>
</svg>
""",
    "disaster": """
<svg role="img" aria-label="Disaster Intelligence. Comparing coverage of Haiti’s 2021 earthquake and Myanmar’s 2025 earthquake." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 118" width="700" height="118">
  <title>Disaster Intelligence. Comparing coverage of Haiti’s 2021 earthquake and Myanmar’s 2025 earthquake.</title>
  <rect width="700" height="118" fill="{bg}"/>
  <g font-family="Georgia, 'Times New Roman', serif" font-size="31" fill="{fg}">
    <text x="33" y="70">Haiti ’21</text>
    <text x="494" y="70">Myanmar ’25</text>
  </g>
  <path d="M223 59H447" stroke="{muted}" stroke-width="1.5"/>
  <circle cx="246" cy="59" r="6" fill="{accent}"/>
  <circle cx="350" cy="59" r="6" fill="{accent}"/>
  <circle cx="424" cy="59" r="6" fill="{accent}"/>
</svg>
""",
    "mips": """
<svg role="img" aria-label="MIPS assembler and simulator. Assembly instructions and register state." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 112" width="340" height="112">
  <title>MIPS assembler and simulator. Assembly instructions and register state.</title>
  <rect width="340" height="112" fill="{bg}"/>
  <rect x="22" y="20" width="296" height="72" rx="4" fill="{tint}"/>
  <g font-family="ui-monospace, Consolas, monospace" font-size="18">
    <text x="36" y="48" fill="{fg}">addi $t0, $zero, 5</text>
    <text x="36" y="76" fill="{accent}">$t0 = 0x00000005</text>
  </g>
</svg>
""",
    "artemis": """
<svg role="img" aria-label="ArtEmis image captioning. Artwork, an emotion input, and a captioning model." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 112" width="340" height="112">
  <title>ArtEmis image captioning. Artwork, an emotion input, and a captioning model.</title>
  <rect width="340" height="112" fill="{bg}"/>
  <rect x="22" y="15" width="85" height="82" rx="3" fill="{tint}"/>
  <circle cx="65" cy="50" r="21" fill="{accent}"/>
  <path d="M29 87L53 63L71 78L88 61L100 87Z" fill="{muted}" opacity=".6"/>
  <g font-family="ui-monospace, Consolas, monospace" font-size="18" fill="{fg}">
    <text x="128" y="49">emotion = awe</text>
    <text x="128" y="77" fill="{accent}">image → caption</text>
  </g>
</svg>
""",
    "discord": """
<svg role="img" aria-label="Discord product workflow. URLs are extracted, validated, and written to Sheets." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 112" width="340" height="112">
  <title>Discord product workflow. URLs are extracted, validated, and written to Sheets.</title>
  <rect width="340" height="112" fill="{bg}"/>
  <path d="M83 56H128M211 56H256" stroke="{muted}" stroke-width="2"/>
  <g font-family="ui-monospace, Consolas, monospace" font-size="17" text-anchor="middle">
    <rect x="13" y="30" width="70" height="52" rx="3" fill="{tint}"/>
    <rect x="128" y="30" width="83" height="52" rx="3" fill="{tint}"/>
    <rect x="256" y="30" width="70" height="52" rx="3" fill="{accent}"/>
    <text x="48" y="62" fill="{fg}">URL</text>
    <text x="169.5" y="62" fill="{fg}">PARSE</text>
    <text x="291" y="62" fill="{on_accent}">SHEET</text>
  </g>
</svg>
""",
    "library": """
<svg role="img" aria-label="Library recommendation. A failed search is enriched with corrections and related titles." xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 112" width="340" height="112">
  <title>Library recommendation. A failed search is enriched with corrections and related titles.</title>
  <rect width="340" height="112" fill="{bg}"/>
  <g font-family="Georgia, 'Times New Roman', serif" font-size="25">
    <text x="24" y="45" fill="{muted}">No results?</text>
    <text x="24" y="80" fill="{accent}">Try these titles.</text>
  </g>
  <g fill="{tint}">
    <rect x="249" y="22" width="13" height="67" rx="2"/>
    <rect x="267" y="15" width="16" height="74" rx="2"/>
  </g>
  <rect x="289" y="31" width="24" height="58" rx="2" fill="{accent}"/>
</svg>
""",
}


def main():
    if ACTIVE_PALETTE not in PALETTES:
        choices = ", ".join(PALETTES)
        raise SystemExit(f"Unknown palette {ACTIVE_PALETTE!r}. Choose one of {choices}.")

    # Prepare both themes before changing any files.
    documents = {}
    for mode in ("light", "dark"):
        colors = PALETTES[ACTIVE_PALETTE][mode]
        for name, value in colors.items():
            if not isinstance(value, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", value):
                raise SystemExit(f"Invalid color for {mode}.{name}. Use a six-digit hex color.")
        for name, template in ARTWORK.items():
            documents[f"{name}-{mode}.svg"] = template.format_map(colors).strip() + "\n"

    destination = Path(__file__).resolve().parent / "assets"
    destination.mkdir(exist_ok=True)
    for filename, document in documents.items():
        (destination / filename).write_text(document, encoding="utf-8")
    print(f"Generated {len(documents)} SVG files using the {ACTIVE_PALETTE!r} palette.")


if __name__ == "__main__":
    main()
