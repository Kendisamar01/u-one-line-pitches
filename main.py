import os
from pathlib import Path

PITCH = "Say the app you keep wishing existed in your own words and let an AI agent on make.fun build a first version you can try; it's a draft, not a leap, so you keep the idea and the final say."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
