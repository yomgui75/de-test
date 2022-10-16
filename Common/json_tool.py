def read_json(path: str):
    import json
    with open(path) as f:
        data = json.load(f)
    return data


def write_json(path: str, d: dict):
    import json
    with open(path, "w") as write_file:
        json.dump(d, write_file, indent=4)
