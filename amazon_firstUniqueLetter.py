import pytest
from collections import Counter

#original function 
def uniqueLetter(name:str) -> str:
    name = name.strip().lower()

    if name == "":
        return ""
    letter_num = Counter(name)
    for letter in name:
        if not letter.isalpha():
            continue
        if (letter_num[letter] == 1):
            return letter

    return ""

@pytest.mark.parametrize("inputs, expected_results", [
    ("Google", "l"),
    ("Amazon", "m"),
    (" 431ddLdw", "l"),
    ("  ", ""),
    ("3213", ""),
    ("xoxoxo", "")])

#test function
def test_uniqueLetter(inputs: str, expected_results:str) -> None:
    actual_result = uniqueLetter(inputs)
    assert actual_result == expected_results, f"Expected {expected_results} but got {actual_result}!"


