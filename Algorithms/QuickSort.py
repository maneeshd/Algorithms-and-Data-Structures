"""
Author: Maneesh Divana <mdaneeshd77@gmail.com>
Interpreter: Python 3.6.8

Quick Sort
Worst Case: O(n^2)
Average Case: O(nlog n)
Best Case: O(nlog n)
"""
from random import shuffle


def partition(arr: list, left: int, right: int) -> int:
    """
    Partitions the given array based on a pivot element,
    then sorts the sub-arrays and returns the partition index
    """
    # Take the right most element as pivot
    pivot = arr[right]

    # i tracks the smallest element, currently invalid
    i = left - 1

    for j in range(left, right):
        # Check if the current element is smaller than pivot element
        if arr[j] <= pivot:
            i += 1
            # If so, swap the smallest element and the current element
            arr[i], arr[j] = arr[j], arr[i]

    # One final swap to put pivot element at its correct position
    arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]

    # Return the partition index
    return i + 1


def qsort(arr: list, left: int, right: int) -> None:
    """
    Recursively partitions the given array and sorts based on
    QuickSort algorithm.
    """
    if left < right:
        # Partition the array and get the partition index
        p_idx = partition(arr, left, right)

        # Recursively partition and sort the sub-arrays
        qsort(arr, left, p_idx - 1)
        qsort(arr, p_idx + 1, right)


if __name__ == "__main__":
    ARR = list(range(0, 10))
    shuffle(ARR)
    LEFT = 0
    RIGHT = len(ARR) - 1
    print("\nQuickSort\n")
    print("Input array:", ARR)
    qsort(ARR, LEFT, RIGHT)
    print("\nSorted array:", ARR, "\n")
