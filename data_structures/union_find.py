class UnionFind(object):
    """Implementation of a Weighted Quick Union with Path Compression stucture.

    This supports fast (approx constant time) unions and finds as well as
    querying for the size of a set, and the number of disjoint sets.

    Sets are represented as ints, so it is up to the user to map whatever type
    they are using (e.g. strings) to ints to use this. This is easily done with:
    
        mapping = {my_thing: i for (i, my_thing) in enumerate(my_iterable)}
        union_find = UnionFind(len(mapping))

    and so on.
    """
    
    def __init__(self, size: int):
        """Inits the Union Find data structure containing |size| members."""
        self._parents = list(range(size))
        self._ranks = [0 for _ in range(size)]
        self._sizes = [1 for _ in range(size)]

    def find(self, i: int) -> int:
        """Finds the representative of set |i|."""
        while i != self._parents[i]:
            self._parents[i] = self._parents[self._parents[i]]
            i = self._parents[i]
        return i

    def union(self, i: int, j: int):
        """Unions the two sets |i| and |j|."""
        x, y = self.find(i), self.find(j)
        if x == y: return

        if self._ranks[x] < self._ranks[y]:
            self._parents[x] = y
        elif self._ranks[x] > self._ranks[y]:
            self._parents[y] = x
        else:
            self._parents[x] = y

        self._sizes[x] += self._sizes[y]
        self._sizes[y] = self._sizes[x]

    def same_set(self, i: int, j: int) -> bool:
        """Checks whether or not the sets |i| and |j| are disjoint or not."""
        return self.find(i) == self.find(j)

    def size_set(self, i: int) -> int:
        """Returns the size of the set |i|."""
        return self._sizes[self.find(i)]
