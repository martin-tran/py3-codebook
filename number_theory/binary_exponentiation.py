from typing import Callable, TypeVar

T = TypeVar('T')


def binary_power(a: T, b: int, iden:T, f: Callable[[T, T], T]) -> T:
    """Computes a^b using exponentiation by squaring for arbitrary monoids.

    Runs in O((b log a)^k) if |f| is implemented in O(d^k) for some fixed k.

    TODO: Figure out how to abstract this to arbitrary semigroups to get rid
      of the need for |iden|.

    Args:
      a: The base we are taking the power of.
      b: The exponent we are taking the power of.
      iden: The identity element of the monoid we are working with.
      f: The associative binary operation taking things of type T to apply |b|
         times to |a|.
    Returns:
      The result of applying |f| to |a| and itself |b| times.
    """
    result = iden
    while b > 0:
        if b & 1:
            result = f(result, a)
        a = f(a, a)
        b >>= 1

    return result
