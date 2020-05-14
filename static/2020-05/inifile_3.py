def loads(string):
    result = {}

    for line in string.splitlines():
        line = line.strip()
        if line.startswith('['):
            section = line.strip('[]')
            result[section] = {}
            currentsection = result[section]
        elif '=' in line:
            key, value = line.split('=')
            key, value = key.strip(), value.strip(' "')
            currentsection[key] = value

    return result
