from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != goal[i]
    )

def solve(start):
    queue = []
    heappush(queue, (heuristic(start), 0, start, []))
    visited = set()

    while queue:
        _, cost, state, path = heappop(queue)

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)
        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for pos in moves:
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            new_state = tuple(new_state)

            if new_state not in visited:
                heappush(
                    queue,
                    (cost + 1 + heuristic(new_state),
                     cost + 1, new_state, path + [state])
                )

    return None

result = solve(start)

if result:
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")
