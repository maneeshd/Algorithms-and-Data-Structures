def is_palindrome(s: str) -> bool:
    """Checks if the given string is a palindrome

    :param s: String to be checked
    :type s: str
    :return: True if the string is a palindrome
             False otherwise
    :rtype: bool
    """
    n = len(s)
    if n <= 1:
        return True
    for i in range(n // 2):
        print(i, s[i], s[n - i - 1])
        if s[i] != s[n - i - 1]:
            return False
    return True


if __name__ == "__main__":
    print(f"Is 'abbaabba' a palindrome? -> {is_palindrome('abbaabba')}")
    print(f"Is 'abbRabba' a palindrome? -> {is_palindrome('abbRabba')}")
