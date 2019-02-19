"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8

Randomized Binary Search :: O(log n)
"""
from random import randint


def get_pivot(num1: int, num2: int) -> int:
    """
    Get a radom pivot between num1 and num2
    """
    return (num1 + randint(0, 1000000) % (num2 - num1 + 1))


def rand_bin_search_recur(arr: list, left: int, right: int, key: int) -> int:
    """
    Recursive Randominzed Binary Search
    """
    if right >= left:
        mid = get_pivot(left, right)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return rand_bin_search_recur(arr, left, mid - 1, key)
        else:
            return rand_bin_search_recur(arr, mid + 1, right, key)
    return -1


def rand_bin_search_iter(arr: list, left: int, right: int, key: int) -> int:
    """
    Iterative Randominzed Binary Search
    """
    while left <= right:
        mid = get_pivot(left, right)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    ARR = list(range(1, 51))
    N = len(ARR)
    KEY = 43

    # Using Recursion
    sidx = rand_bin_search_recur(ARR, 0, N - 1, KEY)
    if sidx == -1:
        print(KEY, "was not found!")
    else:
        print(KEY, "was found at index", sidx)

    # Using Iteration
    sidx = rand_bin_search_iter(ARR, 0, N - 1, KEY)
    if sidx == -1:
        print(KEY, "was not found!")
    else:
        print(KEY, "was found at index", sidx)
