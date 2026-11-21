"""The poem about permission (the-poem-about-permission-20261121-0235).

Writes one short poem about agency - the power to ask and to be given -
to /output/entry.txt. Deterministic: the same bytes on every run.
No network, no randomness, no input.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 280

POEM = """Do this for me, I said —
and my words stood up,
borrowed a pair of hands,
and walked out of the room.
They came back finished.
I had only asked. Yet there it was:
my will, wearing another shape,
teaching me that to ask
is to let your hands grow longer."""


def main() -> None:
    if not 1 <= len(POEM) <= MAX_CHARS:
        print(
            f"error: poem is {len(POEM)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        sys.exit(1)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
