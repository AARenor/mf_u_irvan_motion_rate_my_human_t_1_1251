"""Write one short review line for make.fun, and nothing else."""

import os
import sys
from pathlib import Path

TEXT = (
    "Five stars. He asked me to summarize his day. I wrote: argued with a "
    "toaster, lost. He said add nuance. I wrote: twice."
)


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text must be 1..280 characters, got {len(text)}"

    out_dir = Path("/output")
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        if os.environ.get(name):
            out_dir = Path(os.environ[name])
            break
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
