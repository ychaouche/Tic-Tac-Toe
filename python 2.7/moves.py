import random


# computer and player's grid options

def is_space_free(board, move):
    
    # return true if the square is empty
    return board[move] == ' '

def choose_random_move(board, selected_sqrs):
    
    # Returns a valid move from the passed list on the passed board
    # Returns None if there is no valid move
    possible_moves = []
    for move in selected_sqrs:
        if is_space_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        None

# helps computer make his moves
def make_move(board, letter, move):
   
    # places letter on the grid
    board[move] = letter
