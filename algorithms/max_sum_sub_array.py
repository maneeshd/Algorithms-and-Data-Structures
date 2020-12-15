def max_sum_sub_array(arr, k):
    """Sliding Window"""
    n = len(arr)
    if n < k:
        return -1

    max_sum = -float("inf")
    # 1st window
    window_sum = 0
    for i in range(k):
        window_sum = window_sum + arr[i]
    # Start from k and slide the window
    # to get new sums. Store max and return
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def max_sum_sub_array_naive(arr, k):
    """Naive"""
    n = len(arr)
    if n < k:
        return -1
    max_sum = -float("inf")
    for i in range(n - k + 1):
        cur_sum = 0
        for j in range(k):
            cur_sum = cur_sum + arr[i + j]
        max_sum = max(cur_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    ARR = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    print(max_sum_sub_array_naive(ARR, 4))
    print(max_sum_sub_array(ARR, 4))
