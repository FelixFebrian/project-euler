"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def test_get_sum_of_primes():
    assert get_sum_of_primes(10) == 17
    assert get_sum_of_primes(int(2e6)) == 142913828922


def get_sum_of_primes(n: int) -> int:
    return sum(sieve_of_eratosthenes(n))


def sieve_of_eratosthenes(n: int) -> list:
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        p = prime.index(True, p+1)

    prime[0] = False
    prime[1] = False

    prime_numbers = [i for i, val in enumerate(prime) if val == True]

    return prime_numbers
