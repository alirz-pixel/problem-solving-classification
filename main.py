import sys
from pathlib import Path

import scripts

def load_changed_files(path_str: str):
    path = Path(path_str)
    if not path.exists():
        print(f"[WARN]: {path} not found")
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in lines if l.strip()]


def main():
    if len(sys.argv) < 2:
        print("Usage: test.py changed_files.txt")
        sys.exit(1)

    list_path = sys.argv[1]
    changed_files = load_changed_files(list_path)

    scripts.process_files(changed_files)

if __name__ == "__main__":
    main()
