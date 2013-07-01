import possible_moves, window_handler

def possible_three(grid):
    """(list) -> int

    returns the index of the winning move

    >>> possible_three(["X", "", "", "", "X", "", "", "", ""])
    8
    >>> possible_three(["", "O", "", "", "X", "O", "X", "O", "X"])
    0
    >>> possible_three(["", "O", "", "O", "X", "", "X", "O", "X"])
    0
    """
    
    for square in range(9):
        grid_copy = list(grid)
        if possible_moves.isSpaceFree(grid_copy, square):
            possible_moves.makeMove(grid_copy, window_handler.X, square)
            if window_handler.is_winner(grid_copy, window_handler.X):
                return square

            
if __name__ == '__main__':
    import doctest
    doctest.testmod()
