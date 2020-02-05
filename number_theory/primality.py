from random import randint

from binary_exponentiation import binary_power


def fermat_prime_test(n: int, iterations: int) -> bool:
    """ A probablistic primality test using Fermat's Little Theorem.

    Args:
      n: The number to check for primality.
      iterations: The number of iterations to run the test.
    Returns:
      Whether or not |n| is prime. Like mentioned above, this is probabilistic
      so false-positive may occur, especially if we hit a Carmichael number.
    """
    if n < 4:
        return n == 2 or n == 3

    for _ in range(iterations):
        a = randint(2, n-2)
        if binary_power(a, n-1, 1, lambda x, y: (x*y) % n) != 1:
            return False
    return True
