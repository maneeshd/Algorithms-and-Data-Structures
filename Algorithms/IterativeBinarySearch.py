"""
@author: Maneesh D
@date: 11-Jul-17
@intepreter: Python 3.6

Iterative Binary Search: O(nlog n)
"""
from timeit import default_timer


def iterative_binary_search(data: list, left: int, right: int, key: str) -> int:
    """Iterative Binary Search Implementation"""
    while right >= left:
        mid = (left + right) // 2
        if data[mid] == key:
            return mid
        elif key < data[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main():
    """Main Driver Function"""
    search_key = int(input("Enter the number to search: "))
    data = list(range(1, 1000001))
    start = default_timer()
    index = iterative_binary_search(data, 0, len(data) - 1, search_key)
    end = default_timer()
    if not index == -1:
        print("%d found at index: %d" % (search_key, index))
    else:
        print("!!! %d not found !!!" % search_key)
    print("Time taken to search: %f Seconds" % (end - start))


if __name__ == "__main__":
    print("Iterative Binary Search")
    print("-" * len("Iterative Binary Search"))
    main()
