import os
from pathlib import Path

PITCH = "Say the app you keep wishing existed in your own words and let an AI agent on make.fun build a first draft you can try before you spend a weekend learning to code; you keep the idea, the choices, and the final say."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
