import math
from itertools import permutations, combinations


def is_pandigital(n, from_zero=False):
    if from_zero:
        digits = list(range(0, len(str(n))))
    else:
        digits = list(range(1, len(str(n))+1))
    nums = []
    while n:
        nums.append(n % 10)
        n //= 10
    return sorted(nums) == digits


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def digit_to_num(d):
    return sum([(10**i)*v for i, v in enumerate(reversed(d))])


def digits(n):
    d = []
    while n:
        d.append(n % 10)
        n //= 10
    return d[::-1]
