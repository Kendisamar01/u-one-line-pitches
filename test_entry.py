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
    lines = text.splitlines()
    assert len(lines) == 1, "entry must be exactly one line"
    assert lines[0].strip(), "entry must not be empty or whitespace only"
    assert 1 <= len(lines[0]) <= 240, "entry must be 1 to 240 characters"
    print("PASS")


if __name__ == "__main__":
    main()
