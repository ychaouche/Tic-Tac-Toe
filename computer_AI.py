# import modules
import window_handler
import possible_moves
import winning_move, block

# grids sides and corners
sides = [1, 3, 5, 7]
corners = [0, 2, 6, 8]

def computers_play(grid):
    """(list) -> int

    returns the square where the computer will play next

    >>> computers_play(["", "O", "X", "", "", "O", "", "", "X"])
    4
    >>> computers_play(["X", "O", "", "O", "", "", "X", "", ""])
    4
    >>> computers_play(["0", "", "X", "", "", "O", "", "", "X"])
    6
    >>> computers_play(["", "O", "", "", "X", "O", "X", "O", "X"])
    0
    """

    # AI algorithm
    # First, make it check if computer can win in the next move
    if winning_move.possible_three(grid):
        return winning_move.possible_three(grid)

    # hard coded winning cases for the player
    if ((grid[3] == "O") or (grid[5] == "O")) and ((grid[1] == "O") or (grid[7] == "O")) and grid[4] == "":
        return 4

    # Second, check if player is going to win in the next move and block it
    if block.block(grid):
        return block.block(grid)

    # Third, try to take a corner if its free
    move = possible_moves.chooseRandomMove(grid, corners)
    if move != None:
        return move

    # Move on one of the sides
    return possible_moves.chooseRandomMove(grid, sides)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
