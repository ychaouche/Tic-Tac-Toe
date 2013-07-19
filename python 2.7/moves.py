import random

def choose_random_move(board, moves):
    possible_moves = []
    for move in moves:
        if board.is_space_free(move):
            possible_moves.append(move)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        None
