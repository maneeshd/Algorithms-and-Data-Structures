"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 24/6/17

Linear Search -> O(n)
"""
from timeit import default_timer, Timer


def l_search(data, key):
    for index, value in enumerate(data):
        if value == key:
            print("%d found at index=%d" % (key, index), end="  ->  ")
            return
    print("! Element not found !", end="\t")


def main():
    start = default_timer()
    data = range(0, 1000000)
    l_search(data, 999999)
    print("Search Time = %f Seconds" % (default_timer() - start))


if __name__ == '__main__':
    t = Timer(main)
    avg_time = t.timeit(10) / 10
    print("\nAverage Searching Time = %f Seconds" % avg_time)
