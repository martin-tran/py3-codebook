from typing import Sequence, TypeVar

T = TypeVar('T')

def knuth_morris_pratt(needle: Sequence[T],
                       haystack: Sequence[T]) -> Sequence[int]:
    """Searches for the needle in the haystack of any sequence using KMP.

    Args:
        needle: The pattern to search for.
        haystack: The text to search over.
    Returns:
        A list of the positions of the matches found. These point to the first
        character/index of the match.
    """
    # Precompute the back table.
    n = len(needle)
    backtable = [-1] + [0 for _ in range(n)]
    for i in range(1, n+1):
        position = backtable[i-1]
        while position != -1 and needle[position] != needle[i-1]:
            position = backtable[position]
        backtable[i] = position + 1
        
    # Run the search.
    i, j = 0, 0
    matches = []
    while i < len(haystack):
        while j != -1 and (j == n or haystack[i] != needle[j]):
            j = backtable[j]
        i += 1
        j += 1
        if j == n:
            matches.append(i - j)

    return matches
