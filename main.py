import os
from pathlib import Path

PITCH = "Give an AI agent on make.fun the app idea you've been carrying around; it builds a first draft you can try, you say what to change, and you stay in charge without learning to code."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
