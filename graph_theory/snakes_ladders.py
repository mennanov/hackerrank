"""
Markov takes out his Snakes and Ladders game and stares at the board, and wonders:
If he had absolute control on the die, and could get it to generate any number (in the range 1-6) he desired,
what would be the least number of rolls of the die in which he'd be able to reach the destination square
(Square Number 100) after having started at the base square (Square Number 1)?

Rules:

Markov has total control over the die and the face which shows up every time he tosses it.
You need to help him figure out the minimum number of moves in which he can reach the target square (100) after starting
at the base (Square 1).

A die roll which would cause the player to land up at a square greater than 100, goes wasted,
and the player remains at his original square. Such as a case when the player is at Square Number 99,
rolls the die, and ends up with a 5.

If a person reaches a square which is the base of a ladder, (s)he has to climb up that ladder,
and he cannot come down on it. If a person reaches a square which has the mouth of the snake,
(s)he has to go down the snake and come out through the tail -
there is no way to climb down a ladder or to go up through a snake.
"""
from collections import deque


def snakes_ladders(graph, ladders, snakes):
    # perform a BFS on a graph
    prev = dict()
    queue = deque()
    visited = {0}
    queue.append(0)
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                if u is not None:
                    prev[u] = v
                    queue.append(u)
    # traverse from the final cell to the starting cell
    try:
        node = prev[99]
    except KeyError:
        # route to the final cell is not found
        return -1
    path = []
    while node:
        path.append(node)
        node = prev[node]

    path.reverse()
    rolls = 1
    for p in path:
        # count all non-jump cells
        if p not in ladders and p not in snakes:
            rolls += 1
    return rolls


if __name__ == '__main__':
    import sys

    t = int(sys.stdin.readline().strip())
    for _ in xrange(t):
        graph = []
        ladders = set()
        snakes = set()
        # build a graph (each cell has outgoing edges)
        for i in xrange(100):
            end = 100 if i > 93 else i + 7
            graph.append(range(i + 1, end))
        graph[99] = []
        n = int(sys.stdin.readline().strip())
        for _ in xrange(n):
            # ladders
            start, end = map(int, sys.stdin.readline().strip().split(' '))
            graph[start - 1] = {end - 1}
            ladders.add(start - 1)
        m = int(sys.stdin.readline().strip())
        for _ in xrange(m):
            # snakes
            start, end = map(int, sys.stdin.readline().strip().split(' '))
            graph[start - 1] = {end - 1}
            snakes.add(start - 1)
        print snakes_ladders(graph, ladders, snakes)