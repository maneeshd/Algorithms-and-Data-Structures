def fib(n: int, cache: dict) -> int:
    if n <= 2 and n not in cache:
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1
    if n not in cache:
        cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]


def fib_btm_up(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]


def count_subsets_to_k(arr: list, k: int, i: int) -> int:
    if k == 0:
        return 1
    elif k < 0:
        return 0
    elif i < 0:
        return 0
    elif k < arr[i]:
        return count_subsets_to_k(arr, k, i - 1)
    else:
        return count_subsets_to_k(arr, k - arr[i], i - 1) + count_subsets_to_k(
            arr, k, i - 1
        )


def neighbors(row, col, ROWS, COLS):
    lst = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (
                -1 < row <= ROWS
                and -1 < col <= COLS
                and (row != i or col != j)
                and (0 <= i <= ROWS)
                and (0 <= j <= COLS)
            ):
                lst.append((i, j))
    return lst


def blurFaces(img):
    ROWS = len(img) - 1
    COLS = len(img[0]) - 1

    res = [([0] * COLS)] * ROWS

    for row in range(ROWS):
        for col in range(COLS):
            count = 0
            total = 0
            for r, c in neighbors(row, col, ROWS, COLS):
                total += img[r][c]
                count += 1
            res[row][col] = total / count
    return res


def vehicleDetection(input):
    # comb_arr = []
    # n = len(input)
    # for arr in input:
    #     comb_arr.extend(list(set(arr)))
    # d = {}
    # res = []
    # for i in comb_arr:
    #     if i in d:
    #         d[i] = d[i] + 1
    #         if d[i] == n:
    #             res.append(i)
    #     else:
    #         d[i] = 1
    d = {}
    N = len(input)
    res = []
    for arr in input:
        for num in set(arr):
            if num in d:
                d[num] = d[num] + 1
                if d[num] == N:
                    res.append(num)
            else:
                d[num] = 1

    return res


if __name__ == "__main__":
    # CACHE = dict()
    # print(f"fib(50) = {fib(50, CACHE)}")

    # print(f"fib_btm_up(500) = {fib_btm_up(500)}")

    # ARR = [2, 4, 6, 10]
    # K = 10
    # N = len(ARR) - 1
    # print(f"Number of subsets of {ARR} adding upto {K} is {count_subsets_to_k(ARR, K, N)}")

    mat = [[3, 0, 2, 5], [1, 2, 3, 4], [2, 3, 2, 3]]

    print(blurFaces(mat))
