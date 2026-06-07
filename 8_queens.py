def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < 8:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    
    return True

def solve(board, row, solution):
    if row >= 8:
        solution.append([row[:] for row in board])
        return True
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            solve(board, row + 1,solution)
            board[row][col] = " "
board = [[" " for i in range(8)] for i in range(8)]

solution = []
solve(board,0,solution)
for row in solution[12]:
    print(row)