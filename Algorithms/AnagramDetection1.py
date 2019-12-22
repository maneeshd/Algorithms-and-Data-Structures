"""
Created on: 18-Mar-2018
Created by: Maneesh D
"""


def anagram_checker_1(string_1: str, string_2: str) -> str:
    """Check if the given two strings are anagrams"""
    if len(string_1) != len(string_2):
        return False
    anagram = True
    string_1_dict = {char: False for char in string_1}
    for char in string_1:
        if char in string_2:
            string_1_dict[char] = True
    for char in string_1_dict:
        if not string_1_dict[char]:
            anagram = False
            break
    return anagram


def anagram_checker_2(string_1: str, string_2: str) -> bool:
    """Check if the given two strings are anagrams"""
    string_1_list = list(string_1)
    string_2_list = list(string_2)

    string_1_list.sort()
    string_2_list.sort()

    string_1 = "".join(string_1_list)
    string_2 = "".join(string_2_list)

    return string_1 == string_2


if __name__ == "__main__":
    my_string = "python"
    possible_anagram = "typhon"
    is_anagram = anagram_checker_2(my_string, possible_anagram)
    if is_anagram:
        print("%s and %s are anagrams" % (my_string, possible_anagram))
    else:
        print("%s and %s are not anagrams" % (my_string, possible_anagram))
