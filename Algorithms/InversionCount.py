"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8

Given an unsorted array find the number of
inversions/swaps required to get a sorted array

Method-1: Naive Method O(n^2)

Method-2: Using MergeSort O(nlog n)
"""
from random import shuffle


def naive_inv_count(arr: list) -> int:
    inv_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


def msort_inv_count(arr: list) -> int:
    inv_count = mid = 0
    if len(arr) > 1:
        # Find the mid-point of the array
        mid = len(arr) // 2

        # Divide the array into two parts
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Recursively sort the two parts
        inv_count = msort_inv_count(left_arr)
        inv_count += msort_inv_count(right_arr)

        i = j = k = 0

        # For each element in the two arrays, compare the elements
        # at the same index and replace the original array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                inv_count = inv_count + (mid - i)
            k += 1

        # Copy any elements remaining in the left array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Copy any elements remaining in the right array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    # Return the inversion count
    return inv_count


if __name__ == "__main__":
    ARR = list(range(0, 10))
    shuffle(ARR)
    # ARR = [1, 2, 3, 5, 4, 6, 7, 9, 8]
    print("\nMergeSort\n")
    print("Input array:", ARR)
    INVERSION_COUNT = msort_inv_count(ARR)
    print("\nSorted array:", ARR, "\n")
    print("\nInversion Count =", INVERSION_COUNT, "\n")
