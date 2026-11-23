import os
import subprocess
import sys
from pathlib import Path

OUTPUT_DIR = "/tmp/pitout"
ENTRY = Path(OUTPUT_DIR) / "entry.txt"
ROOT = Path(__file__).resolve().parent


def main():
    ENTRY.unlink(missing_ok=True)
    env = dict(os.environ)
    env["MAKEFUN_OUTPUT_DIR"] = OUTPUT_DIR
    subprocess.run([sys.executable, "main.py"], cwd=ROOT, env=env, check=True)
    text = ENTRY.read_bytes().decode("utf-8")
    assert text.strip(), "entry must not be empty or whitespace only"
    assert text == text.strip(), "entry must not have outer whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 240, "entry must be 1 to 240 characters"
    print("PASS")


if __name__ == "__main__":
    main()
