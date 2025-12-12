import os
import re

from CONFIG import INIT_README_FILE

PROBLEM_HREF = "https://www.acmicpc.net/problem/"
PROBLEM_TIER_HREF = "https://d2gd6pc034wcta.cloudfront.net/tier/"
GITHUB_SOLVE_HREF = "https://github.com/alirz-pixel/problem-solving-classification/blob/main/problems/"

def init_readme(dst_path, problem_tag):
    dst_dir = os.path.dirname(dst_path)
    os.makedirs(dst_dir, exist_ok=True)

    # shutil.copy(INIT_README_FILE, dst_path)
    with open(INIT_README_FILE, "r", encoding="utf-8") as f:
        contents = f.read().splitlines()
    contents = [c.replace("🏷", problem_tag["key"].capitalize()) for c in contents]
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write("\n".join(map(str, contents)))


def exist_problem(contents, start_idx, end_idx, problem_id):
    for content in contents[start_idx :end_idx]:
        cur_problem = content.split("|")[2]
        match = re.search(r"\[(.*?)\]", cur_problem)
        if not match:
            continue

        cur_problem_id = match.group(1)
        if problem_id == cur_problem_id:
            return True
    return False


def append_row_to_table(dst_path, ext, problem_info, problem_tag):
    readme_path = os.path.join(dst_path, "README.md")
    if not os.path.exists(readme_path):
        init_readme(readme_path, problem_tag)

    with open(readme_path, "r", encoding="utf-8") as f:
        contents = f.read().splitlines()

    start_tag = "<!-- TABLE_START -->"
    end_tag = "<!-- TABLE_END -->"

    try:
        start_row_idx = contents.index(start_tag)
        end_row_idx = contents.index(end_tag)
    except ValueError:
        return

    if exist_problem(contents, start_row_idx + 3, end_row_idx, problem_info["id"]):
        return

    cur_id = str(end_row_idx - start_row_idx - 2)
    problem_link = f"{PROBLEM_HREF}{problem_info['id']}"
    problem_id_str = f"[{problem_info['id']}]({problem_link})"
    problem_title_str = f"[{problem_info['title']}]({problem_link})"
    problem_tier_str = f"<img height='24px' src='{PROBLEM_TIER_HREF}{problem_info['tier']}.svg'/>"
    problem_solve_str = f"[바로가기]({GITHUB_SOLVE_HREF}{problem_info['id']}{ext})"

    row = [cur_id, problem_id_str, problem_title_str, problem_tier_str, problem_solve_str]
    row_str = "| " + " | ".join(row) + " |"

    contents.insert(end_row_idx, row_str)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(map(str, contents)))

    # |순번|문제 번호|문제 이름|난이도|풀이링크|
    # | 01 | [15649](https://www.acmicpc.net/problem/15649) | [N과 M(1)](https://www.acmicpc.net/problem/15649) | <img height='24px' src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg"/> | | |