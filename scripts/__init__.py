import os

import scripts.boj
import scripts.project.file_control as file_control
import scripts.project.readme as readme
from CONFIG import PROJECT_DIR

dst_dir = os.path.join(PROJECT_DIR, "classification")

def process_files(changed_files):
    for file_path in changed_files:
        if not "problems" in file_path:
            continue
        print(PROJECT_DIR)
        src_path = os.path.join(PROJECT_DIR, file_path[1:])
        print(f"[Info]: {src_path}")

        problems_infos = boj.get_problem_infos(src_path)
        if not problems_infos:
            continue
        print(f"[Info]: {problems_infos}")

        ext = os.path.splitext(src_path)[1]
        for problem_tag in problems_infos["problem_tags"]:
            dst_path = os.path.join(dst_dir, problem_tag["key"])

            # file_control.copy_file_with_category(src_path, dst_path)
            readme.append_row_to_table(dst_path, ext, problems_infos, problem_tag)
