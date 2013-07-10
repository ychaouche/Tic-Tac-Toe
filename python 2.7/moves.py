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

def make_move(board, letter, move):
    board[move] = letter

def is_winner(board, letter):
    possible_wins = [ [1,2,3], [4,5,6], [7,8,9], [7,4,1], [8,5,2], [9,6,3], [7,5,3], [9,5,1] ]
    for x in possible_wins:
        if board[x[0]] == letter and board[x[1]] == letter and board[x[2]] == letter:
            return True
