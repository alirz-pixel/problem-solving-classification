import os

def get_problem_id(file):
    split_paths = os.path.basename(file)
    return split_paths.split('.')[0]
