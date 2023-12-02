import numpy as np

def create_board_game(rows, cols):
    # Create an empty board with object dtype
    board = np.full((rows, cols), ' ', dtype=object)
    
    # Set top and bottom borders
    board[0, :] = '-'
    board[-1, :] = '-'
    
    # Set left and right borders
    board[:, 0] = '|'
    board[:, -1] = '|'
    
    # Set corners if needed (optional)
    board[0, 0] = board[0, -1] = board[-1, 0] = board[-1, -1] = '+'
    
    return board

def print_board(board):
    for row in board:
        print(''.join(row))

# Example usage
board_size = (10, 10)  # 10 rows and 10 columns
board_game = create_board_game(*board_size)
print_board(board_game)
