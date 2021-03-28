from typing import Optional, Tuple

import math

def extended_euclid(a: int, b: int) -> Tuple[int, int, int]:
    """Computes gcd(a, b) = d = ax + by to return the tuple (d, x, y)."""
    if not b: return (a, 1, 0)

    d, x, y = extended_euclid(b, a%b)
    return (d, y, x - a//b * y)

def inverse_mod(a: int, m: int) -> Optional[int]:
    d, x, y = extended_euclid(a, m)

    if d != 1: return None
    return x
