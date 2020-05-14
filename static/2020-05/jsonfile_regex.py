import re

def loads(json):
    data, idx = parse(json, idx=0)
    return data

def parse(json, idx):
    idx = skip_whitespace(json, idx)

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
        raise ValueError(f"Not a valid JSON string "
                         f"at index {idx}")

    idx = skip_whitespace(json, idx)

    return data, idx

def skip_whitespace(json, idx):
    regex = re.compile("[ \t\n\r]*")
    match = regex.search(json, idx)
    return match.end()

def parse_array(json, idx):
    idx += 1
    array = []
    while True:
        idx = skip_whitespace(json, idx)
        if json[idx] == "]":
            return array, idx+1
        else:
            item, idx = parse_value(json, idx)
            array.append(item)
            if json[idx] == ",":
                idx += 1

def parse_object(json, idx):
    idx += 1
    object = {}
    while True:
        idx = skip_whitespace(json, idx)
        if json[idx] == "}":
            return object, idx+1
        else:
            key, idx = parse_string(json, idx)
            idx = skip_whitespace(json, idx)
            if json[idx] == ":":
                idx += 1
            value, idx = parse_value(json, idx)
            object[key] = value
            if json[idx] == ",":
                idx += 1

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
    regex = re.compile(
        r'"(?P<str>(' # pattern "str" contains:
        r'[^"\\]|'         # any non-["\\], or
        r'\\[/\\bfnrt"]|'  # a simple escape, or
        r'\\u[0-9a-f]{4}'  # a unicode escape
        r')*)"')
    match = regex.search(json, idx)
    string = replace_escapes(match.group("str"))
    return string, match.end()

def replace_escapes(string):
    string = string \
        .replace(r'\"', '"') \
        .replace(r'\\', '\\') \
        .replace(r'\/', '/') \
        .replace(r'\b', '\b') \
        .replace(r'\f', '\f') \
        .replace(r'\n', '\n') \
        .replace(r'\r', '\r') \
        .replace(r'\t', '\t')
    string = re.sub('\\\\u(?P<hex>[0-9a-f]{4})',
                    replace_unicode_escape_in_match,
                    string)
    return string

def replace_unicode_escape_in_match(match):
    hex = match.group("hex")
    return chr(int(hex, 16))

def parse_number(json, idx):
    regex = re.compile(
        '-?(0|[1-9][0-9]*)'   # integer part
        '(\\.?[0-9]*)?'       # fractional part
        '([eE][-+]?[0-9]+)?') # exponent
    match = regex.search(json, idx)
    return float(match.group()), match.end()
