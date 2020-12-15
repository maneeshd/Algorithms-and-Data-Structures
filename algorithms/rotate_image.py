"""
You are given an n x n 2D matrix that represents an image.
Rotate the image by 90 degrees (clockwise).

Example:

For,
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

Note: Try to solve this task in-place (with O(1) additional memory),
since this is what you'll be asked to do during an interview.
"""
from typing import List


def rotate_image(arr: List[list]) -> None:
    """
    Rotates the given n x n matrix by 90 deg clockwise

    :param arr: Image as a 2d matrix
    :type arr: list[list]
    """
    rows = len(arr)
    if rows == 0:
        return
    cols = len(arr[0])

    print("Transpose:")
    for r in range(rows):
        for c in range(r, cols):
            arr[r][c], arr[c][r] = arr[c][r], arr[r][c]
        print(arr[r])

    print("")

    print("90 deg Rotate:")
    for r in range(rows):
        for c in range(cols // 2):
            arr[r][c], arr[r][cols - c - 1] = arr[r][cols - c - 1], arr[r][c]
        print(arr[r])


if __name__ == "__main__":
    ARR = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matrix:")
    for row in ARR:
        print(row)
    print("")
    rotate_image(list(ARR))
