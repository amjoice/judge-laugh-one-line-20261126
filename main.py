"""One-line comedy entry for the make.fun bounty.

Emits a single funny line of at most 200 characters: a sincere
confession to a therapist that gets billed as a no-show. Pure
stdlib, fully deterministic, no network or randomness involved.
"""

from pathlib import Path

_SETUP = "I told my therapist I felt invisible."
_PUNCHLINE = "She charged me for a no-show."
_TARGET = Path("/output/entry.txt")
_MAX_CHARS = 200


def _build_line() -> str:
    """Assemble the entry line from its two beats."""
    return f"{_SETUP} {_PUNCHLINE}"


def _check(text: str) -> str:
    """Return text unchanged when it satisfies the entry gate."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(text) > _MAX_CHARS:
        raise ValueError(f"entry length {len(text)} exceeds {_MAX_CHARS}")
    return text


def _emit(text: str, destination: Path) -> None:
    """Write text to destination, creating parent directories first."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")


def main() -> None:
    line = _check(_build_line())
    _emit(line, _TARGET)


if __name__ == "__main__":
    main()
