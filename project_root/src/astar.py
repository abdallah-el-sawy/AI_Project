import heapq

# Goal state
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]  # 0 represents the blank tile

# Heuristic: Manhattan distance
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(val-1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert state to tuple for hashing
def state_to_tuple(state):
    return tuple(num for row in state for num in row)

# A* search
def a_star(start):
    frontier = []
    heapq.heappush(frontier, (heuristic(start), 0, start, []))
    explored = set()

    while frontier:
        f, g, state, path = heapq.heappop(frontier)
        if state == goal_state:
            return path + [state]
        explored.add(state_to_tuple(state))

        for neighbor in get_neighbors(state):
            if state_to_tuple(neighbor) not in explored:
                heapq.heappush(frontier, (g+1+heuristic(neighbor), g+1, neighbor, path+[state]))
    return None

# Example usage
start_state = [[1,2,3],
                [4,5,0],
                [6,7,8]]

solution = a_star(start_state)

print("Solution steps:")
for step in solution:
    for row in step:
        print(row)
    print()
