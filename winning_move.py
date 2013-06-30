import possible_moves, window_handler

def winning_move(grid):
    """(list) -> int

    returns the index of the winning move

    >>> winning_move(["X", "", "", "", "X", "", "", "", ""])
    8
    >>> winning_move(["", "O", "", "", "X", "O", "X", "O", "X"])
    0
    >>> winning_move(["", "O", "", "O", "X", "", "X", "O", "X"])
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
