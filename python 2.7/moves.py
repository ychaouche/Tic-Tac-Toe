import random

def is_space_free(board, move):
    return board[move] == ' '

def choose_random_move(board, moves):
    possible_moves = []
    for move in moves:
        if is_space_free(board, move):
            possible_moves.append(move)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        None
