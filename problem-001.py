"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6
and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def test_find_sum_of_all_multiples():
    assert find_sum_of_all_multiples(10) == 23
    assert find_sum_of_all_multiples(20) == 78


def find_sum_of_all_multiples(num: int = 1000) -> int:
    sum_of_multiples = sum(x for x in range(num) if x % 3 == 0 or x % 5 == 0)
    return sum_of_multiples


if __name__ == "__main__":
    print(
        "Sum of all the multiples of 3 or 5 below 1000: {}".format(
            find_sum_of_all_multiples(1000)
        )
    )
