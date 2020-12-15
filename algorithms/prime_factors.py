from typing import List


def prime_factors(num: int) -> List[int]:
    if num < 2:
        return []

    if num < 6:
        return [num]

    p_factors = []

    while num % 2 == 0:
        p_factors.append(2)
        num = num // 2

    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            p_factors.append(i)
            num = num // i

    if num > 2:
        p_factors.append(num)

    return p_factors


def unique_prime_factors(num: int) -> List[int]:
    if num < 2:
        return []

    if num < 6:
        return [num]

    p_factors = []

    while num % 2 == 0:
        if 2 not in p_factors:
            p_factors.append(2)
        num = num // 2

    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            if i not in p_factors:
                p_factors.append(i)
            num = num // i

    if num > 2:
        p_factors.append(num)

    return p_factors


if __name__ == "__main__":
    print(f"Prime Factors of 420   : {prime_factors(420)}")
    print(f"Prime Factors of 317   : {prime_factors(317)}")
    print(f"Prime Factors of 10    : {prime_factors(10)}")
    print(f"Prime Factors of 0     : {prime_factors(0)}")
    print(f"Prime Factors of 1     : {prime_factors(1)}")
    print(f"Prime Factors of 2     : {prime_factors(2)}")
    print(f"Prime Factors of 5     : {prime_factors(5)}")
    print(f"Prime Factors of 14782 : {prime_factors(14782)}")
    print("")
    print(f"Unique Prime Factors of 420 : {unique_prime_factors(420)}")
    print(f"Unique Prime Factors of 2147483648 : {unique_prime_factors(2147483648)}")
