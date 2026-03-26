from validators import validate_registration

def test_valid_registration():
    assert validate_registration("AB12CDE") == True

def test_invalid_registration():
    assert validate_registration("123ABC") == False

def test_empty_registration():
    assert validate_registration("") == False