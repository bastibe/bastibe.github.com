def loads(json):
    data, idx = parse(json, idx=0)
    return data

def parse(json, idx):
    if idx >= len(json):
        return {}, idx

    if json[idx] == "{":
        data, idx = parse_object(json, idx)
    elif json[idx] == '[':
        data, idx = parse_array(json, idx)
    elif json[idx] == '"':
        data, idx = parse_string(json, idx)
    elif json[idx] in "-123456789":
        data, idx = parse_number(json, idx)
    elif json[idx] == "t":
        data, idx = parse_true(json, idx)
    elif json[idx] == "f":
        data, idx = parse_false(json, idx)
    elif json[idx] == "n":
        data, idx = parse_null(json, idx)
    else:
        raise ValueError(f"Not a valid JSON string at index {idx}")

    return data, idx

def parse_true(json, idx):
    if json[idx:idx+len("true")] == "true":
        return True, idx+len("true")
    else:
        raise ValueError(
            f'Expected start of "true" at index {idx} '
            f'but found "{json[idx]}"')


def parse_false(json, idx):
    if json[idx:idx+len("false")] == "false":
        return False, idx+len("false")
    else:
        raise ValueError(
            f'Expected start of "false" at index {idx} '
            f'but found "{json[idx]}"')


def parse_null(json, idx):
    if json[idx:idx+len("null")] == "null":
        return None, idx+len("null")
    else:
        raise ValueError(
            f'Expected start of "null" at index {idx} '
            f'but found "{json[idx]}"')
