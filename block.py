import window_handler, possible_moves

def block(grid):
    """(list) -> int

    return the index of the possible win if the opponent places his piece there

    >>> block(["O", "", "", "O", "", "", "", "", ""])
    6
    >>> block(["O", "", "O", "X", "", "", "", "", ""])
    1
    >>> block(["X", "", "X", "O", "O", "", "", "", ""])
    5
    """
    
    for square in range(9):
        grid_copy = list(grid)
        if possible_moves.isSpaceFree(grid_copy, square):
            possible_moves.makeMove(grid_copy, window_handler.O, square)
            if window_handler.is_winner(grid_copy, window_handler.O):
                return square

if __name__ == '__main__':
    import doctest
    doctest.testmod()
