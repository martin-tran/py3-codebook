from typing import Generator, Sequence, TypeVar

T = TypeVar('T')

def lexicographic_permutations(
        a: Sequence[T]) -> Generator[Sequence[T], None, None]:
    """ Algorithm L from Donald Knuth's TAOCP Vol. 4A.

    Generates all permutaitons of |a| in lexicographic order. All variable
    names are stolen straight from the text. This also takes into account
    repeated elements so that only the unique permutations are returned.

    Args:
      a: A sorted sequence of T's from which to generate permutations.

    Returns:
      A generator containing all permutations of iterable in lexicographic
      order.
    """
    if len(a) <= 2:
        for p in [a[:], a[::-1]]:
            yield p
    else:
        p = sorted(a[:])
        n = len(p) - 1

        while True:
            yield p

            j = n - 1
            if j <= 0:
                break

            for i in range(j, -1, -1):
                if p[j] >= p[j+1]:
                    j -= 1
                else:
                    break
            else:
                break

            l = n
            while p[j] >= p[l]:
                l -= 1
            p[j], p[l] = p[l], p[j]
            p = p[:j+1] + p[j+1:][::-1]


            
