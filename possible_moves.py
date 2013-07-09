import random


# computer and player's grid options

def isSpaceFree(board, move):
    """(list, int) -> bool

    compares the given index in a list to an empty string

    >>> isSpaceFree(["", "X"], 0)
    True
    """
    
    # return true if the square is empty
    return board[move] == ' '

def chooseRandomMove(grid, selectedsqrs):
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
    possibleMoves = []
    for move in selectedsqrs:
        if isSpaceFree(grid, move):
            possibleMoves.append(move)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        None

# helps computer make his moves
def makeMove(grid, letter, square):
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
    grid[square] = letter
