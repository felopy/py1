import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(empty_cells)

def main():
    print("Welcome to Tic Tac Toe!")
    mode = input("Do you want to play against the computer? (yes/no): ").lower()

    if mode == "y":
        players = ["X", "O"]
        current_player = 0
        computer_player = 1

        print("You are X. Computer is O.")
        board = [[" " for _ in range(3)] for _ in range(3)]
        print_board(board)

        while True:
            if current_player == 0:
                row = int(input(f"Player {players[current_player]}, enter row (1-3): ")) - 1
                col = int(input(f"Player {players[current_player]}, enter column (1-3): ")) - 1
            else:
                row, col = get_computer_move(board)
                print(f"Computer chooses row {row + 1} and column {col + 1}")
            
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = players[current_player]
                print_board(board)

                if check_winner(board, players[current_player]):
                    if current_player == 0:
                        print(f"Player {players[current_player]} wins!")
                    else:
                        print("Computer wins!")
                    break
                elif is_board_full(board):
                    print("It's a draw!")
                    break

                current_player = 1 - current_player
            else:
                print("Invalid move. Try again.")
    else:
        print("You are Player 1 (X). Player 2 is Player 2 (O).")
        board = [[" " for _ in range(3)] for _ in range(3)]
        print_board(board)
        players = ["X", "O"]
        current_player = 0

        while True:
            row = int(input(f"Player {players[current_player]}, enter row (1-3): ")) - 1
            col = int(input(f"Player {players[current_player]}, enter column (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = players[current_player]
                print_board(board)

                if check_winner(board, players[current_player]):
                    print(f"Player {players[current_player]} wins!")
                    break
                elif is_board_full(board):
                    print("It's a draw!")
                    break

                current_player = 1 - current_player
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    main()

