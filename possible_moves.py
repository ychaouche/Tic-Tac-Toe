# computer and player's grid options

def isSpaceFree(grid, square):
    # return true if the square is empty
    return grid[idx] == ""

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

