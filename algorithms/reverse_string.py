"""
Author: Maneesh Divana <maneeshd77@gmail.com>
Interpreter: Python 3.6.8

Reverse a string without using library functions and extra variable to swap.
"""


def reverse_str(s: str) -> str:
    """Reverse a given string"""
    # Python strings are immutable
    s = list(s)
    s_len = len(s)
    # Using the extra idx as a temp space in list
    s.append(None)
    for idx in range(s_len // 2):
        s[s_len] = s[idx]
        s[idx] = s[s_len - idx - 1]
        s[s_len - idx - 1] = s[s_len]
    return "".join(s)[:s_len]


if __name__ == "__main__":
    print("Reverse('maneesh') = '{0}'".format(reverse_str("maneesh")))
