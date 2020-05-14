import jsonfile

def test_empty():
    assert jsonfile.loads("") == {}

def test_true():
    assert jsonfile.loads("true") == True

def test_false():
    assert jsonfile.loads("false") == False

def test_null():
    assert jsonfile.loads("null") == None

def test_empty_string():
    assert jsonfile.loads('""') == ''

def test_simple_string():
    assert jsonfile.loads('"testing"') == 'testing'

def test_string_with_escapes():
    assert jsonfile.loads('"test\\nting"') == 'test\nting'

def test_all_simple_escapes():
    assert jsonfile.loads(
        '"\\n\\b\\f\\r\\t\\"\\/\\\\"') == \
        '\n\b\f\r\t"/\\'

def test_unicode_escapes():
    assert jsonfile.loads('"test\\u000atest"') == \
        'test\ntest'

def test_simple_number():
    assert jsonfile.loads('42') == 42

def test_complex_number():
    assert jsonfile.loads('-42.1e-5') == -42.1e+5

def test_whitespace():
    assert jsonfile.loads(" 42\t") == 42

def test_array():
    assert jsonfile.loads("[1, 2, 3]") == [1, 2, 3]

def test_object():
    assert jsonfile.loads('{"pi": 3.14, "e": 2.71}') == \
        {'pi': 3.14, 'e': 2.71}

def test_complex_object():
    json = """
    {
      "a": {"pi": 3.14},
      "b": [true, false, null]
    }
    """
    assert jsonfile.loads(json) == {"a": {"pi": 3.14}, "b": [True, False, None]}
