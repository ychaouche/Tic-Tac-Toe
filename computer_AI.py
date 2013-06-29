# import modules
import window_handler
import possible_moves
import winning_move, block

def computers_play(grid):
    # AI algorithm
    # First, make it check if computer can win in the next move
    if winning_move(grid):
        return winning_move(grid)

    # Second, check if player is going to win in the next move and block it
    if block(grid):
        return block(grid)

    # Third, try to take a corner if its free
    move = possible_moves.chooseRandomMoveFromList(grid, [0, 2, 6, 8])
    if move != None:
        return move

    # Take center if it is free
    if possible_moves.isSpaceFree(grid, 4):
        return 4

    # Move on one of the sides
    return possible_moves.chooseRandomMoveFromList(grid, [1, 3, 5, 7])
