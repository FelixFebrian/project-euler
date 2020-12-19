"""
The sum of the squares of the first ten natural numbers is,
    $$1^2 + 2^2 + ... + 10^2 = 385$$

The square of the sum of the first ten natural numbers is,
    $$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$

Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is $3025 - 385 = 2640$.
Find the difference between the sum of the squares of the first one hundred natural num-
bers and the square of the sum.
"""

def test_find_difference_sum_of_squares_and_square_of_sum():
    assert find_difference_sum_of_squares_and_square_of_sum(10) == 2640
    assert find_difference_sum_of_squares_and_square_of_sum(100) == 25164150

def find_difference_sum_of_squares_and_square_of_sum(num: int) -> int:
    """Find the difference between sum of squares and square of sum for the first
    `num` natural numbers.

    Args:
        num (int): First natural numbers.

    Returns:
        int: Difference.
    """
    sum_of_squares = sum(x ** 2 for x in range(1, num+1, 1))
    square_of_sum = sum(range(1, num+1, 1)) ** 2

    return square_of_sum - sum_of_squares
