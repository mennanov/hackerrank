"""
You have an N * M chessboard on which some squares are blocked out.
In how many ways can you place one or more queens on the board, such that, no two queens attack each other?
Two queens attack each other, if one can reach the other by moving horizontally, vertically,
or diagonally without passing over any blocked square. At most one queen can be placed on a square.
A queen cannot be placed on a blocked square.

Input format:
The first line contains the number of test cases T. T test cases follow.
Each test case contains integers N and M on the first line. The following N lines contain M characters each,
and represent a board. A '#' represents a blocked square and a '.' represents an unblocked square.
"""


def place_queen(board, blocked, i, j, n, m):
    get_index = lambda i, j: m * i + j
    # mark rtl horizontally
    for k in xrange(j, -1, -1):
        # unset the bit if not blocked
        index = get_index(i, k)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
    # mark ltr horizontally
    for k in xrange(j + 1, m):
        # unset the bit
        index = get_index(i, k)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
    # mark bottom-up vertically
    for k in xrange(i - 1, -1, -1):
        # unset the bit
        index = get_index(k, j)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
    # mark up-bottom vertically
    for k in xrange(i + 1, n):
        # unset the bit
        index = get_index(k, j)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
    # mark ltr / diagonal
    k, l = i - 1, j + 1
    while k >= 0 and l < m:
        # unset the bit
        index = get_index(k, l)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
        k -= 1
        l += 1
    # mark rtl / diagonal
    k, l = i + 1, j - 1
    while k < n and l >= 0:
        # unset the bit
        index = get_index(k, l)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
        k += 1
        l -= 1
    # mark ltr \ diagonal
    k, l = i + 1, j + 1
    while k < n and l < m:
        # unset the bit
        index = get_index(k, l)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
        k += 1
        l += 1
    # mark rtl \ diagonal
    k, l = i - 1, j - 1
    while k >= 0 and l >= 0:
        # unset the bit
        index = get_index(k, l)
        if blocked & (1 << index) == 1 << index:
            board &= ~(1 << index)
        else:
            break
        k -= 1
        l -= 1
    return board


def memoize(func):
    cache = dict()

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def queens_on_board(board, blocked, n, m, index=0):
    """
    Exponential time algorithm, also consumes a lot of memory (exp) due to memoization.
    """
    places = 0
    if board > 0:
        while index <= (n * m) - 1:
            # check if available
            if board & (1 << index) == 1 << index and blocked & (1 << index) == 1 << index:
                # this cell is available: place queen there and mark diagonal, horizontal and vertical cells as occupied
                i, j = divmod(index, m)
                board_with_queen = place_queen(board, blocked, i, j, n, m)
                places += queens_on_board(board_with_queen, blocked, n, m, index) + 1
            index += 1
    return places % (10 ** 9 + 7)


if __name__ == '__main__':
    import sys

    t = int(sys.stdin.readline())
    for _ in xrange(t):
        n, m = map(int, sys.stdin.readline().strip().split(' '))
        board = 0
        blocked = 0
        c = 0
        for i in xrange(n):
            for s in sys.stdin.readline().strip():
                blocked |= int(s == '.') << c
                board |= 1 << c
                c += 1
        print queens_on_board(board, blocked, n, m)