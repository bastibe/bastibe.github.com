# [Lecture]
# name = Angewandtes Programmieren
# year = 2020
# topic = "File Parsing"

def loads(string):
    result = {}

    for line in string.splitlines():
        line = line.strip()
        if line.startswith(';'):
            continue
        elif line.startswith('['):
            section = line.strip('[]')
            result[section] = {}
            currentsection = result[section]
        elif '=' in line:
            key, value = line.split('=', maxsplit=1)
            key, value = key.strip(), value.strip()
            currentsection[key] = value.strip('"')

    return result
