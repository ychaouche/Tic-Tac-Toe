import random


# computer and player's grid options

def is_space_free(board, move):
    """(list, int) -> bool

    compares the given index in a list to an empty string

    >>> isSpaceFree(["", "X"], 0)
    True
    """
    
    # return true if the square is empty
    return board[move] == ' '

def choose_random_move(board, selected_sqrs):
    """(list, list) -> int

    

    >>> chooseRandomMove(["", "", "", "", "", "", "", "", ""], [2])
    2
    >>> chooseRandomMove(["", "", "", "", "", "", "", "", ""], [7])
    7
    >>> chooseRandomMove(["", "", "", "", "", "", "", "", ""], [1])
    1
    """
    
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
    """(list, str, int) -> None

    mutate a list with the given list, str and index

    >>> abc = ["", "X"]
    >>> makeMove(abc, "O", 1)
    >>> abc
    ['', 'O']
    >>> makeMove(abc, "O", 0)
    >>> abc
    ['O', 'O']
    >>> makeMove(abc, "X", 0)
    >>> abc
    ['X', 'O']
    """
    # places letter on the grid
    board[move] = letter
