"""
Author: Maneesh Divana
Date  : Feb 07, 2020

Longest Common Sub-Sequence

Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

It is a classic computer science problem, the basis of diff (a file comparison program that outputs
the differences between two files), and has applications in bioinformatics.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""
from typing import Tuple, List


def get_all_sub_strings(s: str) -> List[str]:
    """O(N^2)"""
    sub_strings = []
    n = len(s)
    for i in range(n):
        for j in range(1, n - i + 1):
            sub_strings.append(s[i:(i + j)])
    return sub_strings


def get_all_sub_seqs(s: str, idx: int = -1, cur: str = "", seqs: list = None) -> List[str]:
    """O(2^N)"""
    n = len(s)

    if idx == n:
        return seqs

    if seqs is None:
        seqs = []

    seqs.append(cur)

    for i in range(idx + 1, n):
        cur = cur + s[i]
        get_all_sub_seqs(s, i, cur, seqs)

        cur = cur[0: len(cur) - 1]

    return seqs


def naive_lcs(s1: str, s2: str) -> Tuple[str, int]:
    """O(2^M + 2^N + X^2 + Y)"""
    s1_subs = get_all_sub_seqs(s1)  # 2^M
    s2_subs = get_all_sub_seqs(s2)  # 2^N

    common = [s for s in s1_subs if s in s2_subs]   # X^2

    longest = ""
    max_len = 0
    for s in common:    # Y
        s_len = len(s)
        if s_len > max_len:
            max_len = s_len
            longest = s
    # Space: O(M + N + X?)
    return longest, max_len


def dp_lcs_iter(s1: str, s2: str):
    """O(M * N)"""
    m = len(s1)
    n = len(s2)

    tab = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                tab[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                tab[i][j] = tab[i - 1][j - 1] + 1
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])

    return tab[m][n]


def dp_lcs_recr(s1, s2, m, n):
    """O(2^max(M, N))"""
    if m == 0 or n == 0:
        return 0
    elif s1[m - 1] == s2[n - 1]:
        return 1 + dp_lcs_recr(s1, s2, m - 1, n - 1)
    else:
        return max(
            dp_lcs_recr(s1, s2, m - 1, n),
            dp_lcs_recr(s1, s2, m, n - 1)
        )


def dp_lcs_print(s1: str, s2: str):
    """O(M * N)"""
    m = len(s1)
    n = len(s2)

    tab = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                tab[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                tab[i][j] = tab[i - 1][j - 1] + 1
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])

    lcs_len = tab[m][n]

    lcs = [None] * lcs_len

    i = m
    j = n

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs[lcs_len - 1] = s1[i - 1]
            i -= 1
            j -= 1
            lcs_len -= 1
        elif tab[i - 1][j] > tab[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


def longest_common_subsequence(str_1: str, str_2: str) -> Tuple[str, int]:
    str_1_len = len(str_1)
    str_2_len = len(str_2)

    table = [[0 for _ in range(str_2_len + 1)] for _ in range(str_1_len + 1)]

    for row_idx in range(str_1_len + 1):
        for col_idx in range(str_2_len + 1):
            if row_idx == 0 or col_idx == 0:
                table[row_idx][col_idx] = 0
            elif str_1[row_idx - 1] == str_2[col_idx - 1]:
                table[row_idx][col_idx] = 1 + table[row_idx - 1][col_idx - 1]
            else:
                table[row_idx][col_idx] = max(
                    table[row_idx - 1][col_idx],
                    table[row_idx][col_idx - 1]
                )

    lcs_len = table[str_1_len][str_2_len]
    lcs_list = [None] * lcs_len

    row = str_1_len
    col = str_2_len
    idx = lcs_len - 1

    while row > 0 and col > 0:
        if str_1[row - 1] == str_2[col - 1]:
            lcs_list[idx] = str_1[row - 1]
            row = row - 1
            col = col - 1
            idx = idx - 1
        elif table[row - 1][col_idx] > table[row][col - 1]:
            row = row - 1
        else:
            col = col - 1

    return "".join(lcs_list), lcs_len


if __name__ == "__main__":
    # X = "AGGTAB"
    # Y = "GXTXAYB"
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'
    # print("Longest Common Sub-Sequence(naive)  :", naive_lcs(X, Y))
    print("Longest Common Sub-Sequence(dp_iter):", dp_lcs_iter(X, Y))
    # print("Longest Common Sub-Sequence(dp_recr):", dp_lcs_recr(X, Y, len(X), len(Y)))
    print("Longest Common Sub-Sequence(dp_prnt):", dp_lcs_print(X, Y))
    print("Longest Common Sub-Sequence(dp_comp):", longest_common_subsequence(X, Y))
