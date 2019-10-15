from math import fabs
from numbers import Number
from typing import Callable

_EPS = 10**-6

def ternary_search(func: Callable[[Number], Number],
                   left: Number, right: Number, find_min=True):
    """Performs ternary search on |func| to find its extrema.

    Args:
        func: A unimodal function from Number -> Number to ternary search over.
        left: The left bound of the range to search over.
        right: The right bound of the range to search over.
        find_min: Determines if the result to be found is a maximum or minimum.

    Returns:
        The minimum of |func| between |left| and |right| if |find_min| was
        True, or the maximum if |find_min| was False.
    """
    while fabs(right - left) > _EPS:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        f1 = func(m1)
        f2 = func(m2)

        if f1 < f2:
            if find_min:
                right = m2
            else:
                left = m1
        else:
            if find_min:
                left = m1
            else:
                right = m2

    return m1
