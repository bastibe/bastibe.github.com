import jsonfile

def test_empty_string():
    assert jsonfile.loads("") == {}

def test_true():
    assert jsonfile.loads("true") == True

def test_false():
    assert jsonfile.loads("false") == False

def test_null():
    assert jsonfile.loads("null") == None
