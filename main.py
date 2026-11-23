import os
from pathlib import Path

PITCH = "Describe your app idea the way you'd describe it to a friend, and make.fun's AI agent will build a first version you can click through and tweak with you, no code needed."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
