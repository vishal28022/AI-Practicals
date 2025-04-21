import copy 
import random 

def take_input():
    while True:
        try:
            n = int(input("Input size of chessboard? n = "))
            if n <=3:
                print("Enter a value greater than or equal to 4")
                continue
            return n
        except ValueError:
            print("Invalid value entered. Enter again.")

def get_board(n):
    board = ["x"] * n
    for i in range(n):
        board[i] = ["x"] * n
    return board

def print_solution(solutions, n):
    x = random.randint(0, len(solutions) - 1)
    for row in solutions[x]:
        print(" ".join(row))

def solve(board, col, n):
    if col >= n:
        return 
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            if col == n - 1:
                add_solution(board)
                board[i][col] = "x"
                return 
            solve(board, col+1, n)
            board[i][col] = "x"

def is_safe(board, row, col, n):
    for j in range(col):
        if board[row][j] == "Q":
            return False
        
    i, j = row, col
    while i>=0 and j>=0:
        if board[i][j] == "Q":
            return False
        i = i - 1
        j = j - 1

    x, y = row, col
    while x < n and y >= 0:
        if board[x][y] == "Q":
            return False
        x = x + 1
        y = y - 1
    return True

def add_solution(board):
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)

n = take_input()

board = get_board(n)

solutions = []

solve(board, 0, n)

print()
print("One of the solutions is:\n")
print_solution(solutions, n)
print()
print("Total number of solutions = ", len(solutions))