# 8-Puzzle solved using Uniform Cost Search (UCS)

import heapq

# Goal state
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Possible moves and their index changes
moves = {
    'UP': -3,
    'DOWN': 3,
    'LEFT': -1,
    'RIGHT': 1
}

def is_valid_move(zero_index, move):
    if move == 'LEFT' and zero_index % 3 == 0:
        return False
    if move == 'RIGHT' and zero_index % 3 == 2:
        return False
    if move == 'UP' and zero_index < 3:
        return False
    if move == 'DOWN' and zero_index > 5:
        return False
    return True

def apply_move(state, move):
    zero_index = state.index(0)
    new_index = zero_index + moves[move]
    new_state = list(state)
    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
    return tuple(new_state)

def uniform_cost_search(start_state):
    # Priority queue holds (cost, state, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_state, []))

    visited = set()

    while priority_queue:
        cost, state, path = heapq.heappop(priority_queue)

        if state == goal_state:
            return path, cost

        if state in visited:
            continue

        visited.add(state)
        zero_index = state.index(0)

        for move in moves:
            if is_valid_move(zero_index, move):
                next_state = apply_move(state, move)
                if next_state not in visited:
                    # Each move has a uniform cost of 1
                    heapq.heappush(
                        priority_queue,
                        (cost + 1, next_state, path + [move])
                    )

    return None, None


# Initial state
initial_state = (1, 2, 3,
                 4, 5, 0,
                 6, 7, 8)

# Run UCS
solution, total_cost = uniform_cost_search(initial_state)

if solution:
    print("Solution found:")
    print(solution)
    print("Number of moves:", len(solution))
    print("Total cost:", total_cost)
else:
    print("No solution found.")