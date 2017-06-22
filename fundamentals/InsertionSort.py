"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 22/6/17

Insertion Sort
"""


def insertion_sort():
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = key


if __name__ == '__main__':
    data = [31, 41, 59, 26, 41, 58]
    print("Before Sorting: %s" % data)
    insertion_sort()
    print("After Sorting: %s" % data)
