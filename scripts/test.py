# scripts/update_boj.py
import sys
from pathlib import Path

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
    print(f"[INFO]: 파일 path {list_path}")

    changed_files = load_changed_files(list_path)

    print("[INFO]: 변경된 파일 목록:")
    for file in changed_files:
        print(f" - {file}")

if __name__ == "__main__":
    main()
