from typing import Generator

import math

import primality


def pollard_rho(n: int, x0: int = 2, c: int = 1) -> int:
    """Uses Pollard's Rho algorithm to find one prime factor of |n|.

    TODO: This currently uses Floyd's Tortoise & Hare cycle-finding algorithm
      instead of Brent's algorithm. Replace to get better performance.
    """
    tortoise, hare = x0, x0
    factor = 1
    while factor == 1:
        tortoise = ((tortoise * tortoise) % n + c) % n
        hare = ((hare * hare) % n + c) % n
        hare = ((hare * hare) % n + c) % n
        factor = math.gcd(abs(tortoise - hare), n)
    return factor


def factor_integer(n: int) -> Generator[int, None, None]:
    """Returns a generator with the prime factors of |n|.""" 
    n_prime = n
    while not primality.fermat_prime_test(n_prime, 5):
        for (i, j) in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3),
                       (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3)]:
            factor = pollard_rho(n_prime, i, j)
            if factor != n_prime: break
        else:
            break
        n_prime = n_prime // factor
        yield factor
    yield n_prime

