"""
"""


def longest_common_subsequence(str_1: str, str_2: str) -> int:
    str_1_len = len(str_1)
    str_2_len = len(str_2)
    n = max(str_1_len, str_2_len)
    table = [[0] * (n + 1)] * (n + 1)

    for i in range(1, str_1_len + 1):
        for j in range(1, str_2_len + 1):
            if str_1[i - 1] == str_2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[str_1_len][str_2_len]


def k_palindrome(inp_str: str, k: int) -> bool:
    rev_str = inp_str[::-1]  # O(n)
    lcs = longest_common_subsequence(inp_str, rev_str)
    return (len(inp_str) - lcs) <= k


if __name__ == "__main__":
    print(k_palindrome("pqwuzifwovyddwyvvbu", 16))
