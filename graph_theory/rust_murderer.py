"""
Detective Rust is investigating a homicide and he wants to chase down the murderer.
The murderer knows he would definitely get caught if he takes the main roads for fleeing, so he uses the village
roads (or side lanes) for running away from the crime scene.

Rust knows that the murderer will take village roads and he wants to chase him down.
He is observing the city map, but it doesn't show the village roads (or side lanes) on it and shows only the main roads.

The map of the city is a graph consisting N nodes (labeled 1 to N) where a specific given node S represents the
current position of Rust and the rest of the nodes denote other places in the city, and an edge between two nodes
is a main road between two places in the city. It can be suitably assumed that an edge that doesn't exist/isn't
shown on the map is a village road (side lane). That means, there is a village road between two nodes a and b if
there is no city road between them.

Rust wants to calculate the shortest distance from his position (Node S) to all the other places in the city if he
travels using the village roads (side lanes).

Note: The graph/map of the city is ensured to be a sparse graph.
"""

from collections import deque, OrderedDict


def rust_murderer(vertices, start):
    """
    BFS in an implicitly defined graph: edges that are defined in a graph should be avoided,
    meanwhile edges that don't exist should be used.
    """
    dist = dict()
    # instead of having "visited" nodes, we will keep "unvisited" set. It will empty faster than "visited".
    unvisited = set(vertices.keys())
    queue = deque()
    queue.append(start)
    unvisited.remove(start)
    dist[start] = 0
    while queue and unvisited:
        v = queue.popleft()
        for u in unvisited - vertices[v]:
            queue.append(u)
            dist[u] = dist[v] + 1
            unvisited.remove(u)

    return (str(dist[x]) for x in vertices if x != start)


if __name__ == '__main__':
    import sys

    t = int(sys.stdin.readline().strip())
    for _ in xrange(t):
        vertices = OrderedDict()
        n, m = map(int, sys.stdin.readline().strip().split(' '))
        for i in xrange(1, n + 1):
            vertices[i] = set()
        for _ in xrange(m):
            u, v = map(int, sys.stdin.readline().strip().split(' '))
            # add edge from u to v
            vertices[u].add(v)
            # add edge from v to u
            vertices[v].add(u)
        start = int(sys.stdin.readline().strip())
        print ' '.join(rust_murderer(vertices, start))