"""
Author: Maneesh Divana <maneeshd77@gmail.com>

Tower of Hanoi using Recursion

O(n * n!)

For n disks, a total of (2^n) - 1 moves are required.
"""


def toh(n: int, src: str, dst: str, aux: str) -> None:
    if n == 1:
        print("Move disk", n, "from rod", src, "to rod", dst)
        return

    # Move n-1 disks from A to B using C as auxiliary
    toh(n - 1, src, aux, dst)

    # Move the last disk from A to C
    print("Move disk", n, "from rod", src, "to rod", dst)

    # Move the n-1 disks from B to C using A as auxiliary
    toh(n - 1, aux, dst, src)


if __name__ == "__main__":
    N = 4   # Number of disks
    SOURCE = "A"
    AUXILIARY = "B"
    DESTINATION = "C"
    toh(N, SOURCE, AUXILIARY, DESTINATION)
