from typing import List


def permutation(lst: List[int]) -> List[List[int]]:
    n = len(lst)

    if n == 0:
        return []

    if n == 1:
        return [lst]

    p_list = []

    for i in range(n):
        m = lst[i]
        rem_list = lst[:i] + lst[i + 1 :]
        for p in permutation(rem_list):
            p_list.append([m] + p)

    return p_list


def str_permuation(str_: str) -> List[str]:
    n = len(str_)

    if n == 0:
        return []

    if n == 1:
        return [str_]

    p_list = []

    for i in range(n):
        m = str_[i]
        rem_str = str_[:i] + str_[i + 1:]
        for p in str_permuation(rem_str):
            p_list.append(m + p)

    return p_list


if __name__ == "__main__":
    # arr = [1, 2, 3, 4, 5]
    # perms = permutation(arr)
    # for perm in perms:
    #     print(perm)
    # print(len(perms))

    S = "abcd"
    perms = str_permuation(S)
    for perm in perms:
        print(perm)
    print(len(perms))
