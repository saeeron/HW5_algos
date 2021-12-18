import pytest

#original function 
def over_the_road(address: int, n: int) -> int:
    if address%2 == 1:
        return  (n  - ((address - 1)//2))*2
    
    else:
        return  (n  - (address//2)) *2 + 1

# test cases taken from codewars
@pytest.mark.parametrize("inputs, expected_results", [
    ((1, 3), 6),
    ((3, 3), 4),
    ((2, 3), 5),
    ((3, 5), 8),
    ((23633656673, 310027696726), 596421736780)])

#test function
def test_over_the_road(inputs: tuple[int, int], expected_results: list[int]) -> None:
    actual_result = over_the_road(*inputs)
    assert actual_result == expected_results, f"Expected {expected_results} but got {actual_result}!"

