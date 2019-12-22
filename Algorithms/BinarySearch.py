"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8

Binary Search :: O(log n)
"""


def bin_search_recur(arr: list, left: int, right: int, key: int) -> int:
    """Recursive Binary Search"""
    if right >= left:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return bin_search_recur(arr, left, mid - 1, key)
        else:
            return bin_search_recur(arr, mid + 1, right, key)
    return -1


def bin_search_iter(arr: list, left: int, right: int, key: int) -> int:
    """Iterative Binary Search"""
    while left <= right:
        mid = (left + right) // 2
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
    sidx = bin_search_recur(ARR, 0, N - 1, KEY)
    if sidx == -1:
        print(KEY, "was not found!")
    else:
        print(KEY, "was found at index", sidx)

    # Using Iteration
    sidx = bin_search_iter(ARR, 0, N - 1, KEY)
    if sidx == -1:
        print(KEY, "was not found!")
    else:
        print(KEY, "was found at index", sidx)
