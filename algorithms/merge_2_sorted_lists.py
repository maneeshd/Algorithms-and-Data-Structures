from typing import List


def merge_sorted_lists(l1: List[int], l2: List[int]) -> List[int]:
    if not l1 and l2:
        return l2
    elif not l2:
        return l1
    mrg = []
    i = 0
    j = 0
    n1 = len(l1) - 1
    n2 = len(l2) - 1
    while i <= n1 and j <= n2:
        if l1[i] <= l2[j]:
            mrg.append(l1[i])
            i += 1
        else:
            mrg.append(l2[j])
            j += 1
    while i <= n1:
        mrg.append(l1[i])
        i += 1
    while j <= n2:
        mrg.append(l2[j])
        j += 1
    return mrg


if __name__ == "__main__":
    ARR1 = [x for x in range(1, 16, 2)]
    ARR2 = [x for x in range(0, 10)]
    print(f"Array 1: {ARR1}")
    print(f"Array 2: {ARR2}")
    MERGED = merge_sorted_lists(ARR1, ARR2)
    print(f"Merged : {MERGED}")
