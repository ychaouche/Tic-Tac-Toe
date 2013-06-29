# import modules
import window_handler
import possible_moves

def computers_play(grid):
    # AI algorithm
    # First, make it check if computer can win in the next move
    comps_move = False
    for square in range(9):
        grid_copy = list(grid)
        if possible_moves.isSpaceFree(grid_copy, square):
            possible_moves.makeMove(grid_copy, window_handler.comps_le, square)
            if window_handler.is_winner(grid_copy, window_handler.comps_le):
                scorekeeper(window_handler.comps_le)
                return square

    # Second, check if player is going to win in the next move and block it
    for square in range(9):
        grid_copy = list(grid)
        if possible_moves.isSpaceFree(grid_copy, square):
            possible_moves.makeMove(grid_copy, window_handler.plyrs_le, square)
            if window_handler.is_winner(grid_copy, window_handler.plyrs_le):
                return square

    # Third, try to take a corner if its free
    move = possible_moves.chooseRandomMoveFromList(grid, [0, 2, 6, 8])
    if move != None:
        return move

    # Take center if it is free
    if possible_moves.isSpaceFree(grid, 4):
        return 4

    # Move on one of the sides
    return possible_moves.chooseRandomMoveFromList(grid, [1, 3, 5, 7])
