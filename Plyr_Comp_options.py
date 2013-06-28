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

# checks for a winner
def is_winner(gr, le):
    # gr == grid and le == letter, returns True if there is a winner

    return ((gr[0] == le and gr[1] == le and gr[2] == le) or # up the left side
            (gr[0] == le and gr[4] == le and gr[8] == le) or # top left to bottom right diagonally
            (gr[0] == le and gr[3] == le and gr[6] == le) or # top row
            (gr[1] == le and gr[4] == le and gr[7] == le) or # middle row
            (gr[2] == le and gr[5] == le and gr[8] == le) or # bottom row
            (gr[2] == le and gr[4] == le and gr[6] == le) or # top right to bottom left diagonally
            (gr[8] == le and gr[7] == le and gr[6] == le) or # up the right side
            (gr[3] == le and gr[4] == le and gr[5] == le))   # up the middle
