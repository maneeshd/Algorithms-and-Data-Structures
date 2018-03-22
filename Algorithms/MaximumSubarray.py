"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 29/6/17

The Maximum Sub-Array Problem
"""
from sys import maxsize, setrecursionlimit
from timeit import default_timer

setrecursionlimit(1500)


def max_crossing_sub_array(data):
    mid = len(data) // 2
    left_sum = -maxsize - 1
    total = 0
    max_left = 0
    for i in range(mid, -1, -1):
        total = total + data[i]
        if total > left_sum:
            left_sum = total
            max_left = i
    right_sum = -maxsize - 1
    total = 0
    max_right = 0
    for j in range(mid+1, len(data)):
        total = total + data[j]
        if total > right_sum:
            right_sum = total
            max_right = j
    return max_left, max_right, (left_sum + right_sum)


def max_sub_array(data):
    n = len(data)
    if n < 2:
        return 0, n-1,  data[0]
    else:
        mid = n // 2
        left_low, left_high, left_sum = max_sub_array(data[:mid])
        right_low, right_high, right_sum = max_sub_array(data[mid:])
        cross_low, cross_high, cross_sum = max_crossing_sub_array(data)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def main():
    low, high, total = max_sub_array(arg)
    print(
        "The maximun sum contiguous subarray of array is:\n"
        "Start   => %d\n"
        "End     => %d\n"
        "Max-Sum => %d" % (low, high, total))


if __name__ == '__main__':
    print("The Maximum Sub-Array Problem")
    print("-" * len("The Maximum Sub-Array Problem"))
    start = default_timer()
    arg = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    main()
    print("\nExecution Time = %f Seconds" % (default_timer() - start))
