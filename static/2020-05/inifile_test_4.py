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

def test_section_with_quoted_equals():
    string = """
    [section1]
    foo = "something=nasty"
    """
    assert inifile.loads(string) == \
        {'section1': {'foo': 'something=nasty'}}

def test_section_with_quoted_spaces():
    string = """
    [section1]
    foo = " bar "
    """
    assert inifile.loads(string) == \
        {'section1': {'foo': ' bar '}}

def test_comments():
    string = """
    ; this = is a comment
    """
    assert inifile.loads(string) == {}

example_string = """
; last modified 1 April 2001 by John Doe
[owner]
name=John Doe
organization=Acme Widgets Inc.

[database]
; use IP address in case network name resolution is not working
server = 192.0.2.62
port=143
file="payroll.dat"
"""

def integration_test():
    assert inifile.loads(example_string) == {
        'owner': {'name': 'John Doe',
                  'organization': 'Acme Widgets Inc.'},
        'database': {'server': '192.0.2.62',
                     'port': '143',
                     'file': 'payroll.dat'}
    }
