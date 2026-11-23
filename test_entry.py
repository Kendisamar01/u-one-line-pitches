import os
import subprocess
import sys
from pathlib import Path

OUTPUT_DIR = "/tmp/pitout"
ENTRY_PATH = Path(OUTPUT_DIR) / "entry.txt"
ROOT_DIR = Path(__file__).resolve().parent


def main():
    ENTRY_PATH.unlink(missing_ok=True)
    child_env = os.environ.copy()
    child_env["MAKEFUN_OUTPUT_DIR"] = OUTPUT_DIR
    subprocess.run([sys.executable, "main.py"], cwd=ROOT_DIR, env=child_env, check=True)

    entry = ENTRY_PATH.read_text(encoding="utf-8")
    lines = entry.splitlines()
    assert len(lines) == 1, "entry must be exactly one line"
    assert lines[0].strip(), "entry must not be empty or whitespace only"
    assert 1 <= len(lines[0]) <= 240, "entry must be 1 to 240 characters"
    print("PASS")


if __name__ == "__main__":
    main()
