import requests

def get_problem_infos_from_id(problem_id):
    url = "https://solved.ac/api/v3/problem/show"
    querystring = {"problemId":problem_id}

    headers = {
        "x-solvedac-language": "ko",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return None

    json_data = response.json()

    problem_tags = []
    for tags in json_data["tags"]:
        name = ""
        for name_info in tags["displayNames"]:
            if name_info["language"] == "ko":
                name = name_info["name"]
        problem_tags.append({
            "key": tags["key"],
            "name": name
        })
    return {
        "id": problem_id,
        "title": json_data["titleKo"],
        "tier": json_data["level"],
        "problem_tags": problem_tags,
    }


if __name__ == '__main__':
    ret = get_problem_infos_from_id(1235)
    # print(ret)