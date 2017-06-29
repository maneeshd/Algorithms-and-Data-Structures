"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 24/6/17

Worst Case Analysis: Merge Sort -> O(nlog n)
"""
from timeit import Timer, default_timer


def merge_sort(data):
    if len(data) == 1:
        return data
    n = len(data)
    mid = n // 2

    # Divide and sort the sub lists
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    # Merge
    merged = []
    left_len = len(left)
    right_len = len(right)
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] <= right[j]:  # Insert left list element if smaller.
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])  # Insert right list element if smaller.
            j += 1
    while i < left_len:  # Insert the remaining elements in left if any.
        merged.append(left[i])
        i += 1
    while j < right_len:  # Insert the remaining elements in right if any.
        merged.append(right[j])
        j += 1
    return merged


def main():
    start = default_timer()
    data = [i for i in range(100000, 0, -1)]    # Worst Case Input (Reverse Sorted)
    merge_sort(data)
    print("Sort Time = %f Seconds" % (default_timer() - start))


if __name__ == '__main__':
    print("Merge Sort")
    print("-" * len("Merge Sort"))
    t = Timer(main)
    print("\nAverage sorting time for 100000 elements in 10 runs = %f Seconds" % (t.timeit(10) / 10))
