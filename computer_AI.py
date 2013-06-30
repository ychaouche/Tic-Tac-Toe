# import modules
import window_handler
import possible_moves
import winning_move, block

def computers_play(grid):
    # AI algorithm
    # hard coded winning cases for the player
    if ((grid[3] == "O") or (grid[5] == "O")) and ((grid[1] == "O") or (grid[7] == "O")) and grid[4] == "":
        return 4

    # First, make it check if computer can win in the next move
    if winning_move.winning_move(grid):
        window_handler.scorekeeper(window_handler.X)
        return winning_move.winning_move(grid)

    # Second, check if player is going to win in the next move and block it
    if block.block(grid):
        return block.block(grid)

    # Third, try to take a corner if its free
    move = possible_moves.chooseRandomMoveFromList(grid, [0, 2, 6, 8])
    if move != None:
        return move

    # Take center if it is free
    if possible_moves.isSpaceFree(grid, 4):
        return 4

    # Move on one of the sides
    return possible_moves.chooseRandomMoveFromList(grid, [1, 3, 5, 7])
