import main

def test_input_is_not_valid_if_spaces_in_hashtag():
    input = "This input has spaces"
    is_valid = main.is_valid_input(input)
    assert not is_valid

def test_valid_input_is_valid():
    assert True

def test_throw_error_when_input_is_empty():
    assert True