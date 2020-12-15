def binary_search(arr: list, left: int, right: int, key: int) -> int:
    """Iterative Binary Search"""
    if left > right:
        return -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_pivot(arr: list, left, right) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        elif arr[left] >= arr[mid]:
            right = mid
        else:
            left = mid + 1
    return -1


def rotated_binary_search(arr: list, key: int) -> int:
    left = 0
    right = len(arr) - 1
    pivot = find_pivot(arr, left, right)
    if pivot == -1:
        # Not rotated
        return binary_search(arr, left, right, key)

    if arr[pivot] == key:
        return pivot
    elif arr[0] <= key:
        return binary_search(arr, 0, pivot - 1, key)
    return binary_search(arr, pivot + 1, right, key)


def rotated_binary_search_1_pass(arr: list, key: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[left] <= arr[mid]:
            if key >= arr[left] and key <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if key >= arr[mid] and key <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    ARR = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    print(f"Search 7 in {ARR}: {rotated_binary_search_1_pass(ARR, 7)}")
    print(f"Search 3 in {ARR}: {rotated_binary_search_1_pass(ARR, 3)}")
    print(f"Search 9 in {ARR}: {rotated_binary_search_1_pass(ARR, 9)}")
    print(f"Search 1 in {ARR}: {rotated_binary_search_1_pass(ARR, 1)}")
    print(f"Search 0 in {ARR}: {rotated_binary_search_1_pass(ARR, 0)}")
