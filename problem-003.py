"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def test_get_prime_factors():
    pass


def get_prime_factors(num: int = 600851475143) -> list:
    pass



def test_get_factors():
    assert all([num1 == num2 for (num1, num2) in zip(get_factors(2), [1, 2])])
    assert all([num1 == num2 for (num1, num2) in zip(get_factors(3), [1, 3])])
    assert all([num1 == num2 for (num1, num2) in zip(get_factors(4), [1, 2, 4])])
    assert all([num1 == num2 for (num1, num2) in zip(get_factors(5), [1, 5])])


def test_get_largest_prime_factor():
    assert get_largest_prime_factors(2) == 2
    assert get_largest_prime_factors(3) == 3
    assert get_largest_prime_factors(4) == 2
    assert get_largest_prime_factors(5) == 5
    assert get_largest_prime_factors(6) == 3


def get_factors(num: int) -> list:
    """Get the factors of a number.

    Args:
        num (int): the number, for which the factors is to be found.

    Returns:
        list: a list of the factors.
    """
    half: int = num // 2
    factors: list = []
    for iter in range(half, 0, -1):
        if num % iter == 0:
            factors.insert(0, iter)
            if num // iter != iter:
                factors.append(num // iter)

    return factors


def get_largest_prime_factors(num: int = 600851475143) -> int:
    """Get largest prime factors.

    Args:
        num (int, optional): the number, for which the factor is to be found.
            Defaults to 600851475143.

    Returns:
        int: largest prime factor.
    """
    factors = get_factors(num)
    prime_factors: list = []
    for factor in factors:
        if factor not in prime_factors:
            factors_of_factor = get_factors(factor)
            if len(factors_of_factor) == 2:
                prime_factors.append(factor)

    return max(prime_factors)


if __name__ == "__main__":
    print("The largest prime factors of 600851475143: {}".format(
        get_largest_prime_factors()
    ))
