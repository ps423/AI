'''
Q.2) Write a Python program to simulate n-Queens problem.
[20 Marks]
'''

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, board=[], row=0):
    if row == n:
        # Print solution
        for i in range(n):
            line = ""
            for j in range(n):
                if j == board[i]:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            solve_n_queens(n, board + [col], row + 1)

n = int(input("Enter number of queens: "))
print(f"{n}-Queens Problem Solutions:")
solve_n_queens(n)
