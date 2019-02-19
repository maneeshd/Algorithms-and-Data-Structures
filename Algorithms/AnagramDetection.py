"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8

Given two strings, find if they are anagrams of each other.

1. Sort the two strings
2. Compare if the length and element values are same.
"""


def is_anagram(str1: str, str2: str) -> bool:
    str1_list = sorted(str1)
    str2_list = sorted(str2)
    return str1_list == str2_list


if __name__ == "__main__":
    S1 = "heart"
    S2 = "earth"
    IS_ANAGRAM = "Yes" if is_anagram(S1, S2) else "No"
    print("Are", S1, "and", S2, "anagrams? =>", IS_ANAGRAM)
