def loads(string, separator=','):
    result = []

    for line in string.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('#'):
            continue

        values = []
        while True:
            # quoted value:
            if line.strip().startswith('"'):
                quote_start = line.find('"')
                quote_end = line.find('"', quote_start+1)
                value = line[quote_start+1:quote_end]
                rest = line[quote_end+1:]
                _, comma, line = rest.partition(separator)
            # non-quoted value:
            else:
                value, comma, line = line.partition(separator)

            values.append(value)
            if not comma:
                break

        result.append(values)

        if len(result[-1]) != len(result[0]):
            raise ValueError('incorrect number of elements')

    return result
