import inifile

def test_empty_string():
    assert inifile.loads("") == {}

def test_empty_section():
    string = """
    [section1]
    """
    assert inifile.loads(string) == {'section1': {}}
