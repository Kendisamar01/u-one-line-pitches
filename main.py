import os
from pathlib import Path

PITCH = "Tell make.fun's AI agent about the app you keep wishing existed, in plain words, and it will build a first version you can click through and tweak with you—no code to learn, just a few words to try."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
