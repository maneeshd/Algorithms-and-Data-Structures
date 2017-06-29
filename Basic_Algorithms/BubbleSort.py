"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 25/6/17

Worst Case Analysis: Bubble Sort -> O(n^2)
"""
from timeit import Timer, default_timer


def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def main():
    start = default_timer()
    data = [i for i in range(10000, 0, -1)]    # Worst Case - Reverse Sorted
    bubble_sort(data)
    print("Sort Time = %f Seconds" % (default_timer() - start))


if __name__ == '__main__':
    print("Bubble Sort")
    print("-" * len("Bubble Sort"))
    t = Timer(main)
    print("\nAverage worst case sorting time for 10000 elements in 10 runs = %f Seconds" % (t.timeit(10) / 10))
