import os
from pathlib import Path

PITCH = "The fastest way to learn if your app idea works is to stop describing it and start using it: an AI agent on make.fun builds the first version from your words, and you decide what's next."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
