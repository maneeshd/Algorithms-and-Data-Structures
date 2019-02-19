"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8


Check if two strings are k-anagrams or not

Given two strings of lowercase alphabets and a value k,
the task is to find if two strings are K-anagrams of each other or not.

Two strings are called k-anagrams if following two conditions are true.

    Both have same number of characters.
    Two strings can become anagram by changing at most k characters in a string.

Examples :

Input:  str1 = "anagram" , str2 = "grammar" , k = 3
Output:  Yes
Explanation: We can update maximum 3 values and
it can be done in changing only 'r' to 'n'
and 'm' to 'a' in str2.

Input:  str1 = "geeks", str2 = "eggkf", k = 1
Output:  No
Explanation: We can update or modify only 1
value but there is a need of modifying 2 characters.
i.e. g and f in str 2.
"""
from collections import Counter


def is_k_anagram(s1: str, s2: str, k: int) -> bool:
    if len(s1) != len(s2):
        return False, None, None

    counter_map = Counter(s1)
    extra = list()
    changes = 0
    for char in s2:
        if counter_map[char] > 0:
            counter_map[char] -= 1
        else:
            extra.append(char)
            changes += 1

        if changes > k:
            return False, None, None
    diff = [c for c in counter_map if counter_map[c] > 0]
    return True, extra, diff


if __name__ == "__main__":
    STR1 = "anagram"
    STR2 = "grammar"
    K = 3
    RET_VAL, EXTRA, DIFF = is_k_anagram(STR1, STR2, K)
    print("1.",
          STR1,
          "and",
          STR2,
          "can become anagrams with a maximum of",
          K,
          "changes? =>",
          "Yes" if RET_VAL else "No")
    if RET_VAL:
        print("Number of changes required:", len(DIFF))
        print("It can be done by making the below changes in:", STR2)
        for frm, to in zip(EXTRA, DIFF):
            print(frm, "--to-->", to)

    print("")

    STR1 = "maneesh"
    STR2 = "elekshb"
    K = 3
    RET_VAL, EXTRA, DIFF = is_k_anagram(STR1, STR2, K)
    print("2.",
          STR1,
          "and",
          STR2,
          "can become anagrams with a maximum of",
          K,
          "changes? =>",
          "Yes" if RET_VAL else "No")
    if RET_VAL:
        print("Number of changes required:", len(DIFF))
        print("It can be done by making the below changes in:", STR2)
        for frm, to in zip(EXTRA, DIFF):
            print(frm, "--to-->", to)

    print("")

    STR1 = "shazam"
    STR2 = "lkbzam"
    K = 2
    RET_VAL, EXTRA, DIFF = is_k_anagram(STR1, STR2, K)
    print("3.",
          STR1,
          "and",
          STR2,
          "can become anagrams with a maximum of",
          K,
          "changes? =>",
          "Yes" if RET_VAL else "No")
    if RET_VAL:
        print("Number of changes required:", len(DIFF))
        print("It can be done by making the below changes in:", STR2)
        for frm, to in zip(EXTRA, DIFF):
            print(frm, "--to-->", to)
