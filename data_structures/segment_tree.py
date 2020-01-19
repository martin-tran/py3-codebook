from typing import Callable, Sequence, TypeVar

T = TypeVar('T')


class SegmentTree(object):
    """Implementation of a 1-D segment tree for arbitrary binary operations.
    
    This currently only supports things of type T where T and the binary
    operation form a semigroup. The identity element defaults to 0 for basic
    use in range sum queries so this can be easily used when T is any basic
    number type, i.e., ints and floats.

    Attributes:
      tree: The array representing the binary tree containing the segment tree.
    """
    def __init__(self,
                 array: Sequence[T],
                 combine: Callable[[T, T], T],
                 identity: T = 0):
        """Inits a Segment Tree for a range of size |n|.
        
        Args:
          array: An array of type T to build the segment tree out of.
          combine: A binary operation combining the left child with the
            right when building the tree. It is recommended to use a
            commutative operation to avoid any confusion of the order
            of combining.
          identity: This must be the identity element of the monad formed by
            elements of type T and |combine|.
        """
        self._combine = combine
        self._identity = identity
        self._n = len(array) - 1
        tree = [identity for _ in range(self._n * 4)]

        def _build(vertex: int, left: int, right: int):
            if left == right:
                tree[vertex] = array[left]
            else:
                middle = (left + right) // 2
                _build(vertex * 2, left, middle)
                _build(vertex * 2 + 1, middle + 1, right)
                tree[vertex] = combine(tree[vertex * 2], tree[vertex * 2 + 1])

        _build(1, 0, self._n)
        self.tree = tree

    def range_query(self, left: int, right: int) -> T:
        """Queries the segment tree in the range [left, right]."""
        return self._range_query(1, 0, self._n, left, right)

    def _range_query(self, vertex: int, left_bound: int, right_bound: int,
                     left_query: int, right_query: int) -> T:
        if left_query > right_query:
            return self._identity
        if left_query == left_bound and right_query == right_bound:
            return self.tree[vertex]
        middle = (left_bound + right_bound) // 2

        return self._combine(
            self._range_query(vertex * 2, left_bound, middle, left_query,
                              min(right_query, middle)),
            self._range_query(vertex * 2 + 1, middle + 1, right_bound,
                              max(left_query, middle + 1), right_query))

    def update(self, index: int, value: T):
        """Updates the range at index |i| with |value|."""
        self._update(1, 0, self._n, index, value)

    def _update(self, vertex: int, left: int, right: int, index: int,
                value: T):
        if left == right:
            self.tree[vertex] = value
        else:
            middle = (left + right) // 2
            if index <= middle:
                self._update(vertex * 2, left, middle, index, value)
            else:
                self._update(vertex * 2 + 1, middle + 1, right, index, value)

            self.tree[vertex] = self._combine(self.tree[vertex * 2],
                                              self.tree[vertex * 2 + 1])
