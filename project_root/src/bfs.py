from collections import deque

start = [
    [5, 6, 8],
    [0, 4, 7],
    [1, 3, 2]
]

def is_goal(board):
    N = len(board)
    count = 1
    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                if board[i][j] != 0:
                    return False
            else:
                if board[i][j] != count:
                    return False
            count += 1
    return True

def get_steps(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                row, col = i, j

    steps = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        r, c = row + dr, col + dc
        if 0 <= r < N and 0 <= c < N:
            new_board = [r[:] for r in board]
            new_board[row][col], new_board[r][c] = new_board[r][c], new_board[row][col]
            steps.append(new_board)
    return steps

def solve(start):
    queue = deque([(start, [])])
    visited = set()  

    while queue:
        board, path = queue.popleft()
        board_tuple = tuple(tuple(row) for row in board)  
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        if is_goal(board):
            return path + [board]

        for step in get_steps(board):
            queue.append((step, path + [board]))

# Running
solution = solve(start)

for step in solution:
    for row in step:
        print(row)
    print("-----")
