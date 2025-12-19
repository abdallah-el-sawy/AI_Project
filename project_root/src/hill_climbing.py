
import copy

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def hill_climbing(initial_state):
    current = initial_state

    while True:
        h_current = heuristic(current)
        print("Current State (h =", h_current, ")")
        for row in current:
            print(row)
        print("-----------")

        if current == goal_state:
            print("Goal Reached!")
            return

        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=heuristic)

        if heuristic(next_state) >= h_current:
            print("Stuck at local optimum!")
            return

        current = next_state


if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    hill_climbing(initial_state)
