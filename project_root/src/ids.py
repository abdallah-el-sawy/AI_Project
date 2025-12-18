# 8-Puzzle using Iterative Deepening Search


# Step 1: States
initial_state = [
    1, 2, 3,
    4, 5, 0,
    6, 7, 8
]

goal_state = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]

#------------------------------------------------------------------------------------

# Step 2: Find empty tile
def find_zero(state):
    return state.index(0)

#------------------------------------------------------------------------------------

# Step 3: Get valid moves
def get_valid_moves(zero_index):
    moves = []

    row = zero_index // 3
    col = zero_index % 3

    if row > 0:
        moves.append("UP")
    if row < 2:
        moves.append("DOWN")
    if col > 0:
        moves.append("LEFT")
    if col < 2:
        moves.append("RIGHT")

    return moves

#------------------------------------------------------------------------------------


# Step 4: Apply move
def apply_move(state, move):
    new_state = state.copy() # copy to avoid modifying the original state during DFS Expansion
    zero_index = find_zero(state)

    if move == "UP":
        swap_index = zero_index - 3
    elif move == "DOWN":
        swap_index = zero_index + 3
    elif move == "LEFT":
        swap_index = zero_index - 1
    elif move == "RIGHT":
        swap_index = zero_index + 1

    new_state[zero_index], new_state[swap_index] = (
        new_state[swap_index],
        new_state[zero_index],
    )

    return new_state

#------------------------------------------------------------------------------------

# Step 5: Goal test
def is_goal(state):
    return state == goal_state

#------------------------------------------------------------------------------------

# Step 6: Depth-Limited Search
def depth_limited_search(state, depth, path, visited):
    if is_goal(state):
        return path

    if depth == 0:
        return None

# visited -> set -> no list -> لازم حاجه ثابته -> from list to tuple
    visited.add(tuple(state))

# Expansion
    for move in get_valid_moves(find_zero(state)):
        new_state = apply_move(state, move)

        if tuple(new_state) not in visited:
            result = depth_limited_search(
                new_state,
                depth - 1,
                path + [move],
                visited
            )
            if result is not None:
                return result

    visited.remove(tuple(state))
    return None

#------------------------------------------------------------------------------------

# Step 7: Iterative Deepening Search
def iterative_deepening_search(initial_state, max_depth=20):
    for depth in range(max_depth + 1):
        visited = set()
        result = depth_limited_search(
            initial_state,
            depth,
            [],
            visited
        )
        if result is not None:
            return result, depth

    return None, None

# Step 8: Run the algorithm
solution, depth_found = iterative_deepening_search(initial_state)

if solution:
    print("Solution found!")
    print("Depth:", depth_found)
    print("Moves:", solution)
else:
    print("No solution found.")
