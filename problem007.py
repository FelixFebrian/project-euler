"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th
prime is 13.

What is the 10001st prime number?
"""

from math import log


def test_find_nth_prime_number():
    assert find_nth_prime_number(6) == 13
    assert find_nth_prime_number(10001) == 104743  # Solution to Problem!


def find_nth_prime_number(n: int) -> int:
    """Find the nth prime number.

    Args:
        n (int): index of the prime number

    Returns:
        int: the nth prime number
    """
    upper_bound = int(n * (log(n) + log(log(n))))
    primes = list(range(2, upper_bound))
    for idx in range(int(n ** (0.5) + 1)):
        primes = list(filter(lambda x: x % primes[idx] or x == primes[idx], primes))

    return primes[n - 1]
