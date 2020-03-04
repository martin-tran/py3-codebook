import codebook.data_structures

from typing import Dict, List, Tuple, Union


Number = Union[int, float]


def kruskals(graph: Tuple[Number, Number, Number],
             n: int) -> Tuple[Dict[int,  List[Tuple[int, int]]], int]:
    """Use Kruskal's algorithm to find the minimum spanning tree of |graph|.

    Args:
      graph: The weighted graph on which to find the MST. This should be
        represented by 3-tuples (u, v, w) denoting an edge between node u and v
        with weight w. Vertices should be labelled by integers in the range
        [0, n).
      n: The number of vertices of |graph|.
    Returns:
      The tuple of the subgraph which is an MST of |graph| in adjacency list
      form and the total cost of the MST.
    """
    graph.sort(key=lambda edge: edge[2])
    forest = data_structures.UnionFind(n)
    mst = {i:[] for i in range(n)}
    cost = 0

    for (u, v, w) in graph:
        if forest.same_set(u, v): continue
        forest.union(u, v)
        mst[u].append((v, w))
        mst[v].append((u, w))
        cost += w

    return (mst, cost)

"""
Example graph from https://en.wikipedia.org/wiki/Minimum_spanning_tree#/media/File:Msp-the-cut-correct.svg

Usage: kruskals(g, 6)

g = [(0, 1, 1), (1, 0, 1), (0, 3, 3), (3, 0, 3),
     (1, 2, 6), (2, 1, 6), (1, 3, 5), (3, 1, 5), (1, 4, 1), (4, 1, 1),
     (2, 4, 5), (4, 2, 5), (2, 5, 2), (5, 2, 2),
     (3, 4, 1), (4, 3, 1),
     (4, 5, 4), (5, 4, 4)]
"""
