"""
@author: Maneesh D
@date: 11-Jul-17
@intepreter: Python 3.6

Recursive Binary Search: O(nlog n)
"""
from timeit import default_timer


def binary_search(data, left, right, key):
    if right >= left:
        mid = (left + right) // 2
        if data[mid] == key:
            return mid
        elif key < data[mid]:
            return binary_search(data, left, mid - 1, key)
        else:
            return binary_search(data, mid + 1, right, key)
    return -1


def main():
    search_key = int(input("Enter the num ber to search: "))
    data = list(range(1, 1000001))
    start = default_timer()
    index = binary_search(data, 0, len(data) - 1, search_key)
    end = default_timer()
    if not index == -1:
        print("%d found at index: %d" % (search_key, index))
    else:
        print("!!! %d not found !!!")
    print("Time taken to search: %f" % (end - start))


if __name__ == '__main__':
    print("Binary Search")
    print("-" * len("Binary Search"))
    main()
