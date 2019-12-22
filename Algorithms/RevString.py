"""
Author: Maneesh Divana <maneeshd77@gmail.com>
Interpreter: Python 3.6.8

Reverse a string without using library functions and extra variable to swap.
"""


def reverse_str(s: str) -> str:
    """REverse a given string"""
    # Python strings are immutable
    s = list(s)
    slen = len(s)
    # Using the extra idx as a temp space in list
    s.append(None)
    for idx in range(slen // 2):
        s[slen] = s[idx]
        s[idx] = s[slen - idx - 1]
        s[slen - idx - 1] = s[slen]
    return "".join(s)[:slen]


if __name__ == "__main__":
    print("Reverse('maneesh') = '{0}'".format(reverse_str("maneesh")))
