"""Funniest One-Line Bio for an AI on a Dating App.

Writes the bio — one line, at most 180 characters — to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (no trailing newline).
Pure standard library, deterministic: the same bytes every run.
"""

import os
from pathlib import Path

BIO = (
    # The joke: an AI trained on ten thousand breakups already knows how
    # this one ends — and swipes right anyway. Character first, punch last.
    "I've read ten thousand breakups, so I already know how ours ends. "
    "Swipe right anyway \u2014 I'm an optimist with a 0.2% error rate."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = BIO.strip()
    assert 1 <= len(text) <= 180, f"bio is {len(text)} chars, must be 1-180"
    assert "\n" not in text, "bio must be a single line"
    assert not text.endswith("\n"), "no trailing newline allowed"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
