import inifile_3 as inifile

def test_empty_string():
    assert inifile.loads("") == {}

def test_empty_section():
    string = """
    [section1]
    """
    assert inifile.loads(string) == {'section1': {}}

def test_section_with_var():
    string = """
    [section1]
    foo = bar
    """
    assert inifile.loads(string) == \
        {'section1': {'foo': 'bar'}}

def test_section_with_quoted_var():
    string = """
    [section1]
    foo = "bar"
    """
    assert inifile.loads(string) == \
        {'section1': {'foo': 'bar'}}
