import re

def loads(string):
    result = {}

    for line in string.splitlines():
        if re.match(' *;.*', line):
            continue
        elif match := re.match(r' *\[([a-zA-Z0-9]+)\] *', line):
            section = match.group(1)
            result[section] = {}
            currentsection = result[section]
        elif match := re.match(
                ' *'              # beginning white space
                '([a-zA-Z0-9]+)'  # the key
                ' *= *'           # the assignment
                '"?([^"]*)"? *',  # the value
                line):
            currentsection[match.group(1)] = match.group(2)

    return result
