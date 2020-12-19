"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from
1 to 20?
"""

from collections import Counter
from problem003 import get_prime_factors


def test_find_smallest_divisible_number():
    assert find_smallest_divisible_number(10) == 2520
    assert find_smallest_divisible_number(20) == 232792560


def find_smallest_divisible_number(max_num: int) -> int:
    """
    Find the smallest number that can be divided by every integers between 1 and max_num

    Args:
        max_num (int): maximum of integer

    Returns:
        int: the smallest divisible number
    """
    common_primes: dict = dict()
    for num in range(max_num, 2, -1):
        primes = Counter(get_prime_factors(num))
        for (prime_number, times) in primes.items():
            if not prime_number in common_primes.keys():
                common_primes[prime_number] = times
            else:
                common_primes[prime_number] = max(times, common_primes[prime_number])

    divisible_number = 1
    for (key, val) in common_primes.items():
        divisible_number *= key ** val

    return divisible_number
