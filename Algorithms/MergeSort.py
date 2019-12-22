"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8

Merge Sort
Worst Case: O(nlog n)
Average Case: O(nlog n)
Best Case: O(nlog n)
"""
from random import shuffle


def msort(arr: list) -> None:
    """Recursive MergeSort implementation"""
    if len(arr) > 1:
        # Find the mid-point of the array
        mid = len(arr) // 2

        # Divide the array into two parts
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Recursively sort the two parts
        msort(left_arr)
        msort(right_arr)

        i = j = k = 0

        # For each element in the two arrays, compare the elements
        # at the same index and replace the original array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
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


if __name__ == "__main__":
    ARR = list(range(0, 10))
    shuffle(ARR)
    print("\nMergeSort\n")
    print("Input array:", ARR)
    msort(ARR)
    print("\nSorted array:", ARR, "\n")
