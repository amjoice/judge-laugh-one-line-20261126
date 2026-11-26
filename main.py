"""One-line comedy entry for the make.fun bounty.

Emits a single funny line of at most 200 characters: a sincere
confession to a therapist that gets billed as a no-show. Pure
stdlib, fully deterministic, no network or randomness involved.
"""

import os

_PARTS = (
    "I told my therapist I felt invisible. ",
    "She charged me for a no-show.",
)
LINE = "".join(_PARTS)
OUTPUT_PATH = "/output/entry.txt"


def _validate(text: str) -> None:
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} outside gate 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")


def main() -> None:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
