"""
A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def test_is_palindrome():
    assert is_palindrome(111) == True
    assert is_palindrome(121) == True
    assert is_palindrome(1221) == True
    assert is_palindrome(12321) == True
    assert is_palindrome(12333) == False


def test_get_largest_palindrome():
    assert get_largest_palindrome(2) == 9009


def is_palindrome(num: int) -> bool:
    input_num = num
    reversed_num = 0
    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10

    if input_num == reversed_num:
        return True
    else:
        return False


def get_largest_palindrome(number_of_digits: int) -> int:
    floor = 10 ** number_of_digits
    ceil = 10 ** (number_of_digits + 1)
    largest_palindrome = -1
    for first_num in range(ceil, floor, -1):
        for second_num in range(ceil, floor, -1):
            num = first_num * second_num
            if is_palindrome(num) and num > largest_palindrome:
                largest_palindrome = num

    return largest_palindrome
