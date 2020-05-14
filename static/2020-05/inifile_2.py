def loads(string):
    result = {}

    for line in string.splitlines():
        line = line.strip()
        if line.startswith('['):
            section = line.strip('[]')
            result[section] = {}

    return result
