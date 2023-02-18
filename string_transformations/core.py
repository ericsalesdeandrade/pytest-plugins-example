import time


def count_vowels(sentence: str) -> int:
    """
    Count the number of vowels in a sentence
    :param sentence: The sentence to count the vowels in
    :return: The number of vowels in the sentence
    """
    vowels = "aeiou"
    count = 0
    for letter in sentence.lower():
        if letter in vowels:
            count += 1
    return count


def remove_spaces_in_string(sentence: str, delay_length: int) -> str:
    """
    Remove spaces in a string
    :param delay_length: Duration of the delay
    :param sentence: The sentence to remove spaces in
    :return: The sentence without spaces
    """
    delay(length=delay_length)
    return sentence.replace(" ", "")


def delay(length: int) -> None:
    time.sleep(length)
