"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the pro-
duct abc.
"""

def test_get_product_of_triplet():
    assert get_product_of_triplet() == 31875000


def get_product_of_triplet() -> int:
    triplet = dict()
    for b in range(2, 500):
        for a in range(1, b):
            c = 1000 - (a + b)
            if (c ** 2) == (a ** 2) + (b ** 2):
                triplet.update({"a": a, "b": b, "c": c})

        if triplet:
            break

    return triplet["a"] * triplet["b"] * triplet["c"]
