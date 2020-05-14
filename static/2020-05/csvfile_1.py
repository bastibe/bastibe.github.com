def loads(string):
    result = []

    for line in string.splitlines():
        line = line.strip()
        if not line:
            continue
        items = line.split(',')
        result.append(items)

    return result
