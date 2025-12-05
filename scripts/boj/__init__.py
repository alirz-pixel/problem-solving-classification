from .problem import get_problem_id
from .solved_ac import get_problem_infos_from_id

def get_problem_infos(file):
    problem_id = get_problem_id(file)
    problems_infos = get_problem_infos_from_id(problem_id)
    return problems_infos