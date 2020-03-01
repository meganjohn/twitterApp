import main

def test_valid_input_is_valid():
    input = "thisisavalidinput"
    is_valid = main.is_valid_input(input)
    assert is_valid

def test_input_is_not_valid_if_spaces_in_hashtag():
    input = "This input has spaces"
    is_valid = main.is_valid_input(input)
    assert not is_valid

def test_input_is_not_valid_when_input_is_empty():
    input = ""
    is_valid = main.is_valid_input(input)
    assert not is_valid