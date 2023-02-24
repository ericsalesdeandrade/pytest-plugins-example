from string_transformations.core import count_vowels, remove_spaces_in_string


def test_count_vowels():
    assert count_vowels("Python") == 1
    assert count_vowels("Theistareykjarbunga") == 7
    assert count_vowels("grrrrgh!") == 0
    assert (
        count_vowels(
            "Github is the second best thing that "
            "happened to programmers, after the keyboard!"
        )
        == 22
    )
    assert count_vowels("A nice day to code!") == 7


def test_remove_spaces_in_string_no_delay():
    assert remove_spaces_in_string("Python", 0) == "Python"
    assert (
        remove_spaces_in_string("This is a random string", 0) == "Thisisarandomstring"
    )
    assert (
        remove_spaces_in_string("This is a random string with numbers 1234567890", 0)
        == "Thisisarandomstringwithnumbers1234567890"
    )


def test_remove_spaces_in_string_delay():
    assert remove_spaces_in_string("Python", 2) == "Python"
    assert (
        remove_spaces_in_string("This is a random string", 2) == "Thisisarandomstring"
    )
    assert (
        remove_spaces_in_string("This is a random string with numbers 1234567890", 2)
        == "Thisisarandomstringwithnumbers1234567890"
    )


def test_remove_spaces_in_string_mock_delay(mocker):
    mocker.patch("string_transformations.core.delay", return_value=None)
    assert (
        remove_spaces_in_string("This is a random string", 3) == "Thisisarandomstring"
    )
