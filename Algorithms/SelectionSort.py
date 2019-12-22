"""
@author: Maneesh D
@date: 11-Jul-17
@intepreter: Python 3.6

Worst Case Analysis: Selection Sort -> O(n^2)
"""
from timeit import Timer, default_timer
from random import shuffle


ARR = list()


def selection_sort(data):
    """Selection sort implementation"""
    for i in range(len(data)):
        min_pos = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_pos]:
                min_pos = j
        data[i], data[min_pos] = data[min_pos], data[i]


def main():
    """Main Driver Function"""
    start = default_timer()
    shuffle(ARR)
    print("Input Array:", ARR)
    selection_sort(ARR)
    print("Sorted Array:", ARR)
    print("Sorting Time: %f Seconds\n" % (default_timer() - start))


if __name__ == "__main__":
    print("Selection Sort")
    print("-" * len("Selection Sort"))
    ARR = list(range(25, 0, -1))  # Worst Case Input(Reverse Sorted)
    t = Timer(main)
    print(
        "\nAverage sorting time for 25 elements in 3 runs = %f Seconds"
        % (t.timeit(3) / 3)
    )
