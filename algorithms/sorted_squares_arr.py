def sorted_squares_arr_naive(arr: list) -> list:
    for idx, num in enumerate(arr):
        arr[idx] = num ** 2
    arr.sort()
    return arr


def sorted_squares_arr(arr: list) -> list:
    n = len(arr)
    out = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(arr[left]) > abs(arr[right]):
            out[i] = arr[left] ** 2
            left += 1
        else:
            out[i] = arr[right] ** 2
            right -= 1
    return out


if __name__ == "__main__":
    ARR = [-7, -3, -1, 3, 4, 8]
    ssa = sorted_squares_arr(list(ARR))
    print(f"Sorted Squares Array: {ARR} -> {ssa}")
