"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 24/6/17

Linear Search -> O(n)
"""
from timeit import default_timer, Timer


def linear_search(data: list, key: str) -> None:
    for index, value in enumerate(data):
        if str(value) == str(key):
            print("%d found at index=%d" % (key, index), end="  ->  ")
            return
    print("! Element not found !", end="\t")


def main():
    """Main Driver Function"""
    start = default_timer()
    linear_search(arg, 1000000)
    print("Search Time: %f Seconds" % (default_timer() - start))


if __name__ == "__main__":
    t = Timer(main)
    arg = list(range(1, 1000001))
    avg_time = t.timeit(10) / 10
    print("\nAverage Searching Time = %f Seconds" % avg_time)
