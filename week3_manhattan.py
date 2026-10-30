
import heapq

goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]


def heuristic(state):
    h = 0

    for i in range(3):
        for j in range(3):
            tile = state[i][j]

            if tile != 0:
                x = (tile - 1) // 3
                y = (tile - 1) % 3

                h += abs(i - x) + abs(j - y)

    return h


def get_neighbors(state):
    neighbors = []

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_state = [r[:] for r in state]

            new_state[row][col], new_state[r][c] = \
                new_state[r][c], new_state[row][col]

            neighbors.append(new_state)

    return neighbors


def astar(start):
    pq = [(heuristic(start), 0, start)]
    visited = set()

    while pq:
        f, g, state = heapq.heappop(pq)

        key = tuple(tuple(row) for row in state)

        if key in visited:
            continue

        visited.add(key)

        print("State:")
        for row in state:
            print(row)

        print("g =", g, "h =", heuristic(state), "f =", f)
        print()

        if state == goal:
            print("Goal reached!")
            print("Total moves:", g)
            return

        for neighbor in get_neighbors(state):
            new_key = tuple(tuple(row) for row in neighbor)

            if new_key not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    print("No solution found!")


start = [[2, 8, 3],
         [1, 6, 4],
         [7, 0, 5]]

astar(start)
