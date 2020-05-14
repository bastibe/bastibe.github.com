import csvfile

def test_empty_string():
    assert csvfile.loads("") == []

def test_single_line():
    string = """
    a,b,c
    """
    assert csvfile.loads(string) == [['a', 'b', 'c']]

def test_multi_line():
    string = """
    a,b,c
    d,e,f
    """
    assert csvfile.loads(string) == [['a', 'b', 'c'],
                                     ['d', 'e', 'f']]

def test_empty_item():
    string = """
    a,,
    """
    assert csvfile.loads(string) == [['a', '', '']]

def test_item_with_space():
    string = """
    a, b ,c
    """
    assert csvfile.loads(string) == [['a', ' b ', 'c']]

def test_quoted_item():
    string = """
    "a","b","c"
    """
    assert csvfile.loads(string) == [['a', 'b', 'c']]

def test_quoted_item_with_comma():
    string = """
    "a","b,b","c"
    """
    assert csvfile.loads(string) == [['a', 'b,b', 'c']]

def test_quoted_item_with_space():
    string = """
    "a", "b"," c"
    """
    assert csvfile.loads(string) == [['a', 'b', ' c']]
