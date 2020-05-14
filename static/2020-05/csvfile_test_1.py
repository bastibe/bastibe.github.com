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
