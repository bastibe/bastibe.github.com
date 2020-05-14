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

def parse_string(json, idx):
    start = idx
    idx += 1
    string = ""
    while True:
        print(idx, repr(json[idx]))
        if json[idx] == '"':
            return string, idx+1
        elif json[idx] == '\\':
            if json[idx+1] == 'n':
                string += '\n'
                idx += 2
            elif json[idx+1] == 'b':
                string += '\b'
                idx += 2
            elif json[idx+1] == 'f':
                string += '\f'
                idx += 2
            elif json[idx+1] == 'r':
                string += '\r'
                idx += 2
            elif json[idx+1] == 't':
                string += '\t'
                idx += 2
            elif json[idx+1] == '"':
                string += '"'
                idx += 2
            elif json[idx+1] == '/':
                string += '/'
                idx += 2
            elif json[idx+1] == '\\':
                string += '\\'
                idx += 2
            elif (json[idx+1] == 'u' and
                  json[idx+2] in '0123456789abcdef' and
                  json[idx+3] in '0123456789abcdef' and
                  json[idx+4] in '0123456789abcdef' and
                  json[idx+5] in '0123456789abcdef'):
                string += chr(int(json[idx+2:idx+6], 16))
                idx += 6
            else:
                string += json[idx]
                idx += 1
        else:
            string += json[idx]
            idx += 1

def parse_number(json, idx):
    start = idx

    if json[idx] == "-":
        idx += 1
    while idx < len(json) and json[idx] in "0123456789":
        idx += 1
    if idx < len(json) and json[idx] == ".":
        idx += 1
    while idx < len(json) and json[idx] in "0123456789":
        idx += 1
    if idx < len(json) and json[idx] in "eE":
        idx += 1
    if idx < len(json) and json[idx] in "-+":
        idx += 1
    while idx < len(json) and json[idx] in "0123456789":
        idx += 1

    return float(json[start:idx]), idx
