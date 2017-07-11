"""
@author: Maneesh D
@date: 11-Jul-17
@intepreter: Python 3.6

Worst Case Analysis: Selection Sort -> O(n^2)
"""
from timeit import Timer, default_timer


def selection_sort(data):
    for i in range(len(data)):
        min_pos = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_pos]:
                min_pos = j
        data[i], data[min_pos] = data[min_pos], data[i]


def main():
    start = default_timer()
    data = [i for i in range(10000, 0, -1)]    # Worst Case Input(Reverse Sorted)
    selection_sort(data)
    print("Sort Time = %f Seconds" % (default_timer() - start))


if __name__ == '__main__':
    print("Selection Sort")
    print("-" * len("Selection Sort"))
    main()
    t = Timer(main)
    print("\nAverage sorting time for 10000 elements in 10 runs = %f Seconds" % (t.timeit(10)/10))
