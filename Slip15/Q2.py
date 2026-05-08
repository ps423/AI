'''
Q.2) Write a Python program to solve tic-tac-toe problem.
[20 Marks]
'''

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    for turn in range(9):
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player
                    
                    if check_win(board, player):
                        print_board(board)
                        print(f"Player {player} wins!")
                        return
                    
                    player = "O" if player == "X" else "X"
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Invalid position. Enter values between 0-2.")
        except ValueError:
            print("Please enter valid numbers.")
    
    print_board(board)
    print("It's a draw!")

tic_tac_toe()
