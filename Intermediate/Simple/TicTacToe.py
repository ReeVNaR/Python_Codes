def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

board = [[" "]*3 for _ in range(3)]
turn = "X"

for _ in range(9):
    print_board(board)
    try:
        row, col = map(int, input(f"Player {turn}, enter row and column (0-2): ").split())
        if row not in range(3) or col not in range(3):
            print("Invalid input! Row and column must be between 0 and 2.")
            continue
    except ValueError:
        print("Invalid input! Please enter two integers separated by a space.")
        continue
    
    if board[row][col] == " ":
        board[row][col] = turn
        if check_winner(board):
            print_board(board)
            print(f"Player {turn} wins!")
            break
        turn = "O" if turn == "X" else "X"
    else:
        print("Cell already taken! Try again.")

else:
    print_board(board)
    print("It's a tie!")
