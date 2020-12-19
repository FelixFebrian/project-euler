"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def test_get_prime_factors():
    """Test for get_prime_factors() function."""
    assert all([a == b for (a, b) in zip(get_prime_factors(2), [2])])
    assert all([a == b for (a, b) in zip(get_prime_factors(3), [3])])
    assert all([a == b for (a, b) in zip(get_prime_factors(4), [2, 2])])
    assert all([a == b for (a, b) in zip(get_prime_factors(5), [5])])
    assert all([a == b for (a, b) in zip(get_prime_factors(6), [2, 3])])
    assert all([a == b for (a, b) in zip(get_prime_factors(7), [7])])
    assert all([a == b for (a, b) in zip(get_prime_factors(8), [2, 2, 2])])
    assert all([a == b for (a, b) in zip(get_prime_factors(9), [3, 3])])
    assert all([a == b for (a, b) in zip(get_prime_factors(10), [2, 5])])
    assert all([a == b for (a, b) in zip(get_prime_factors(100), [2, 2, 5, 5])])


def get_prime_factors(num: int = 600851475143) -> list:
    """Get prime factor(s) of a number.

    Args:
        num (int, optional): the number, for which the prime factor(s) is to be found.
            Defaults to 600851475143.

    Returns:
        list: list of prime factor(s).
    """
    prime_factors: list = []
    sqrt_of_num = num ** (1 / 2)
    for divider in range(2, round(sqrt_of_num) + 1, 1):
        while num % divider == 0:
            prime_factors.append(divider)
            num = num // divider

    if num != 1:
        prime_factors.append(num)

    return prime_factors


if __name__ == "__main__":
    print(f"The largest prime factors of 600851475143: {max(get_prime_factors())}")
