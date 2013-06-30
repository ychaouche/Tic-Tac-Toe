import random

# turns
comps_turn = True
plyrs_turn = False

# computer and player's grid options

def isSpaceFree(grid, square):
    """(list, int) -> bool

    compares the given index in a list to an empty string

    >>> isSpaceFree(["", "X"], 0)
    True
    """
    
    # return true if the square is empty
    return grid[square] == ""

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

# switch turns
def switch_turns():
    global comps_turn, plyrs_turn

    comps_turn, plyrs_turn = plyrs_turn, comps_turn

# no more moves
def dead_game():
    global comps_turn, plyrs_turn

    comps_turn = False
    plyrs_turn = False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
