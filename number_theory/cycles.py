from typing import Callable, TypeVar

T = TypeVar('T')

def floyd(f: Callable[[T], T], x0: T) -> bool:
    tortoise = x0
    hare = f(x0)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    return true
