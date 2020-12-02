import json

def get_json(input):
    if type(input) is tuple:
        input = input[0]
    try:
        return json.loads(input)
    except (ValueError, TypeError):
        if is_file(input):
            f = open(input, "r")
            return json.loads(f.read())
        elif is_json(input):
            return json.loads(json.dumps(input))
        else:
            raise ValueError("ERROR: Please input a valid JSON string or a file containing valid JSON")


def is_json(input):
    try:
        json.dumps(input)
        return True
    except (ValueError, TypeError):
        return False


def is_file(input):
    try:
        f = open(input, "r")
        return is_json(f.read())
    except (FileNotFoundError, TypeError):
        return False