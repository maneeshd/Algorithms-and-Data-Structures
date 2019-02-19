"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8

Count characters at same position as in English alphabet.

Given a string of lower and uppercase characters, the task is to
find that how many characters are at same position as in English alphabet.

Examples:

Input:  ABcED
Output :  3
First three characters are at same position
as in English alphabets.

Input:  geeksforgeeks
Output :  1
Only 'f' is at same position as in English
alphabet

Input :  alphabetical
Output :  3
"""


def find_count(str_: str) -> tuple:
    count = 0
    ord_l = ord("a")
    ord_u = ord("A")
    chars = list()
    for i in range(len(str_)):
        ord_s = ord(str_[i])
        if i == (ord_s - ord_l) or i == (ord_s - ord_u):
            count += 1
            chars.append(str_[i])
    return count, chars


if __name__ == "__main__":
    S1 = "ABcED"
    COUNT, CHARS = find_count(S1)
    print("String:", S1)
    print("Number of characters at the same position as in English alphabet:", COUNT)
    print(", ".join(CHARS), "is/are at the same position as in English alphabets.\n")

    S2 = "geeksforgeeks"
    COUNT, CHARS = find_count(S2)
    print("String:", S2)
    print("Number of characters at the same position as in English alphabet:", COUNT)
    print(", ".join(CHARS), "is/are at the same position as in English alphabets.\n")

    S3 = "alphabetical"
    COUNT, CHARS = find_count(S3)
    print("String:", S3)
    print("Number of characters at the same position as in English alphabet:", COUNT)
    print(", ".join(CHARS), "is/are at the same position as in English alphabets.\n")
