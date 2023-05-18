import pytest

def binary_search(arr, x):
    left = 0
    right = len(arr) 
    while left < right:
        mid = round((left + right) / 2)
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid           
    return -1

@pytest.fixture
def arr():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_binary_search_found(arr):
    assert binary_search(arr, 5) == 4


def test_binary_search_not_found(arr):
    assert binary_search(arr, 10) == -1


@pytest.mark.parametrize("x,result", [
    (1, 0),
    (5, 4),
    (9, 8),
    (10, -1)
])


def test_binary_search_parametrized(arr, x, result):
    assert binary_search(arr, x) == result
