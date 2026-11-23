import os
from pathlib import Path

PITCH = "Before you spend a weekend learning to code, tell your app idea to an AI agent on make.fun and let it put a first version in front of you: a draft, not a promise, with you still in charge."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
