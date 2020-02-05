from typing import Sequence


def eratosthenes(n: int) -> Sequence[int]:
    """Implementation of Sieve of Eratosthenes retruning all primes upto |n|.

    This sieves only the odd numbers up to sqrt(n). Runs in O(n log log n).
    """
    primes = [True for _ in range(n+1)]
    primes[0] = False
    primes[1] = False

    for j in range(4, n+1, 2):
        primes[j] = False
        
    i = 3
    while i * i < n+1:
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
        i += 2
        
    return primes
