from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("AB123") == True
    assert is_valid("XY9") == True

def test_invalid_plates():
    assert is_valid("50CS") == False        # starts with number
    assert is_valid("C") == False           # too short
    assert is_valid("ABCDEFG") == False     # too long
    assert is_valid("AB012") == False       # starts number with 0
    assert is_valid("AB12C") == False       # letters after number
    assert is_valid("AB.12") == False       # special character
    assert is_valid("AB 12") == False       # space
    assert is_valid("A") == False           # insufficient length
    assert is_valid("1") == False
    assert is_valid("A1") == False