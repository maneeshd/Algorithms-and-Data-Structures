"""
Author: Maneesh Divana <maneeshd77@gmail.com>

Some problems where binary seach can be applied
"""
from typing import List


def is_x_a_square(x: int) -> bool:
    """Is x a square number?"""
    if x == 0:
        return False
    left = 1
    right = x
    while left <= right:
        mid = left + (right - left) // 2
        if mid ** 2 == x:
            return True
        elif mid ** 2 < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


def my_sqrt(x: int) -> int:
    """Implement int sqrt(int x)
    https://leetcode.com/problems/sqrtx/

    Compute and return the square root of x,
    where x is guaranteed to be a non-negative integer.

    Since the return type is an integer, the decimal digits
    are truncated and only the integer part of the result is returned.
    """
    if x == 0:
        return 0
    if x < 4:
        return 1

    left = 2
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid ** 2 < x:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1


def gte_x_search(lst: List[int], x: int) -> int:
    """First number in lst which is >= x"""
    left = 0
    right = len(lst) - 1
    if right == -1:
        return -1
    if right == 0:
        return lst[0] if lst[0] >= x else -1
    lst.sort()  # can be removed is lst is guarenteed to be sorted
    cur_n = 0
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] >= x:
            cur_n = lst[mid]
            right = mid - 1
        else:
            left = mid + 1
    return cur_n


def lte_x_search(lst: List[int], x: int) -> int:
    """First number in lst which is <= x"""
    left = 0
    right = len(lst) - 1
    if right == -1:
        return -1
    if right == 0:
        return lst[0] if lst[0] <= x else -1
    lst.sort()  # can be removed is lst is guarenteed to be sorted
    cur_n = 0
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] <= x:
            cur_n = lst[mid]
            left = mid + 1
        else:
            right = mid - 1
    return cur_n


if __name__ == "__main__":
    print(f"Is 4 a square number?         -> {is_x_a_square(4)}")
    print(f"Is 9 a square number?         -> {is_x_a_square(9)}")
    print(f"Is 10 a square number?        -> {is_x_a_square(10)}")
    print(f"Is 144 a square number?       -> {is_x_a_square(144)}")
    print(f"Is 10000 a square number?     -> {is_x_a_square(10000)}")
    print(f"Is 1000000 a square number?   -> {is_x_a_square(1000000)}")
    print(f"Is 178182738 a square number? -> {is_x_a_square(178182738)}")

    print(f"Is 0 a square number?         -> {is_x_a_square(0)}")
    print(f"Is 1 a square number?         -> {is_x_a_square(1)}")

    ARR = [2, 3, 6, 5, 8, 10, 12]
    print(f"First number >= 9 -> {gte_x_search(ARR, 9)}")
    print(f"First number <= 9 -> {lte_x_search(ARR, 9)}")
