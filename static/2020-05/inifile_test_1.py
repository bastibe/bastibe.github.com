import inifile

def test_empty_string():
    assert inifile.loads("") == {}
