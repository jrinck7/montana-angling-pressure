"""
Post-processes nbconvert's LaTeX output so the notebook's title cell
renders as an actual document title instead of a numbered section.

Why this is needed:
Your top markdown cell is an H1 ("A River Runs through COVID-19:")
followed by an H3 subtitle. nbconvert turns markdown headers into
LaTeX \section / \subsubsection commands, so they show up numbered
("1", "1.0.1") right under the real \title/\maketitle block. If you
instead put both lines in a single markdown header, the whole string
becomes one \section{...} line, and at 0.5in margins it's too wide
for one line, so LaTeX's default hyphenation breaks a word to make
it fit - that's the mid-word hyphen you were seeing.

This script:
  1. Replaces the auto-generated \title{Project1_JansenRinck} with a
     proper two-line title (main title + smaller subtitle), using an
     explicit \\ line break so nothing gets hyphenated.
  2. Deletes the redundant \section/\subsubsection heading pair that
     nbconvert generated from the markdown title cell, so it doesn't
     also appear as a numbered heading in the body.

Run this on the .tex file after `jupyter nbconvert --to latex` and
before `xelatex`.
"""

import re
import sys


def fix_title(tex: str) -> str:
    # 1. Give the document a real two-line title instead of the filename.
    tex = tex.replace(
        r"\title{Project1\_JansenRinck}",
        "\\title{A River Runs through COVID-19:\\\\[6pt]\n"
        "{\\normalsize\\mdseries How the Pandemic Redistributed "
        "Angling Pressure Across Montana}}",
    )

    # 2. Remove the redundant numbered heading nbconvert built from the
    #    same text (the \hypertarget/\section/\subsubsection pair).
    #    Matched loosely (DOTALL) so it survives nbconvert re-wrapping
    #    the heading text across different line lengths.
    pattern = re.compile(
        r"\\hypertarget\{a-river-runs-through-covid-19\}.*?"
        r"\\label\{how-the-pandemic-redistributed-angling-pressure-across-montana\}\}\n?",
        re.DOTALL,
    )
    tex, n = pattern.subn("", tex)
    if n == 0:
        print(
            "Warning: title heading block not found/removed - "
            "check that the notebook's title cell text hasn't changed.",
            file=sys.stderr,
        )

    return tex


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_title.py <path-to-tex-file>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = fix_title(content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Title fixed in {path}")
