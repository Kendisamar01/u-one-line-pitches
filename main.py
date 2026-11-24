import os
from pathlib import Path

PITCH = "If you've ever said 'I wish there were an app that...' out loud, hand that wish to an AI on make.fun: it builds a first version you can tap through and tell it what to change; if it's not the one, you've spent a wish and kept the idea."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
