import random

# turns
comps_turn = True
plyrs_turn = False

# computer and player's grid options

def isSpaceFree(grid, square):
    # return true if the square is empty
    return grid[square] == ""

def chooseRandomMoveFromList(grid, movesList):
    # Returns a valid move from the passed list on the passed board
    # Returns None if there is no valid move
    possibleMoves = []
    for move in movesList:
        if isSpaceFree(grid, move):
            possibleMoves.append(move)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        None

# helps computer make his moves
def makeMove(grid, letter, square):
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
