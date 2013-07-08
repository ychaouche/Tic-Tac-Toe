import possibleMoves



def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
# All Moves
            # Winning Top Row
    if (board[1] == computerLetter and board[2] == computerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;
    if (board[1] == computerLetter and board[3] == computerLetter) and possibleMoves.isSpaceFree(board,2):
        return 2;
    if (board[2] == computerLetter and board[3] == computerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;

            # Winning Second Row
    if (board[4] == computerLetter and board[5] == computerLetter) and possibleMoves.isSpaceFree(board,6):
        return 6;
    if (board[4] == computerLetter and board[6] == computerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[6] == computerLetter) and possibleMoves.isSpaceFree(board,4):
        return 4;

        # Winning Third Row
    if (board[7] == computerLetter and board[8] == computerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[7] == computerLetter and board[9] == computerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;
    if (board[8] == computerLetter and board[9] == computerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;

        # Winning First Column

    if (board[1] == computerLetter and board[4] == computerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[1] == computerLetter and board[7] == computerLetter) and possibleMoves.isSpaceFree(board,4):
        return 4;
    if (board[4] == computerLetter and board[7] == computerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;

        # Winning Second Column
    if (board[2] == computerLetter and board[5] == computerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;
    if (board[2] == computerLetter and board[8] == computerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[8] == computerLetter) and possibleMoves.isSpaceFree(board,2):
        return 2;

        # Winning Third Column
    if (board[3] == computerLetter and board[6] == computerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[3] == computerLetter and board[9] == computerLetter) and possibleMoves.isSpaceFree(board,6):
        return 6;
    if (board[6] == computerLetter and board[9] == computerLetter) and possibleMoves.isSpaceFree(board,3):
        return 4;

        # Winning Left to Right Diagonal
    if (board[1] == computerLetter and board[5] == computerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[1] == computerLetter and board[9] == computerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[9] == computerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;

        # Winning Right to Left Diagonal
    if (board[3] == computerLetter and board[5] == computerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[3] == computerLetter and board[7] == computerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[7] == computerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;

            # Top Row Horizontal Blocking
    if (board[1] == playerLetter and board[2] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;
    if (board[2] == playerLetter and board[3] == playerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;
    if (board[1] == playerLetter and board[3] == playerLetter) and possibleMoves.isSpaceFree(board,2):
        return 2;

            # Second Row Horizontal Blocking
    if (board[4] == playerLetter and board[5] == playerLetter) and possibleMoves.isSpaceFree(board,6):
        return 6;
    if (board[5] == playerLetter and board[6] == playerLetter) and possibleMoves.isSpaceFree(board,4):
        return 4;
    if (board[4] == playerLetter and board[6] == playerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;

            # Third Row Horizontal Blocking
    if (board[7] == playerLetter and board[8] == playerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[8] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[7] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;

            # First Column Vertical Blocking
    if (board[1] == playerLetter and board[4] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[4] == playerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;
    if (board[1] == playerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,4):
        return 4;

            # Second Column Vertical Blocking
    if (board[2] == playerLetter and board[5] == playerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;
    if (board[5] == playerLetter and board[8] == playerLetter) and possibleMoves.isSpaceFree(board,2):
        return 2;
    if (board[2] == playerLetter and board[8] == playerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;

            # Third Column Vertical Blocking
    if (board[3] == playerLetter and board[6] == playerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[3] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,6):
        return 6;
    if (board[6] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;

            # Left to Right Diagonal
    if(board[1] == playerLetter and board[5] == playerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if(board[1] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;
    if(board[5] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;

            # Right to Left Diagonal
    if (board[3] == playerLetter and board[5] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[3] == playerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,5):
        return 5;
    if (board[5] == playerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;

        # Take Center if it's Free
    if possibleMoves.isSpaceFree(board, 5):
        return 5

        # Counteract if they form a diagonal with PL in 5 and in 9
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,6):
        return 6;
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;

        # Counteract if they form a diagonal with PL in 5 and in 1
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and possibleMoves.isSpaceFree(board,2):
        return 2;
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and possibleMoves.isSpaceFree(board,4):
        return 4;
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;

        # Counteract if they form a diagonal with PL in 5 and in 7
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,4):
        return 4;
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;

        # Counteract if a diagonal with CL in 5 and PL in 1 & 9
    if (board[1] == playerLetter and board[5] == computerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,2):
        return 2;
    if (board[1] == playerLetter and board[5] == computerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;


        # Counteract if diagonal with CL in 5 and PL in 3 & 7
    if (board[3] == playerLetter and board[5] == computerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,2):
        return 2;
    if (board[3] == playerLetter and board[5] == computerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,8):
        return 8;


    if (board[2] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;
    if (board[2] == playerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;
    if (board[6] == playerLetter and board[1] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;
    if (board[6] == playerLetter and board[7] == playerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[4] == playerLetter and board[3] == playerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;
    if (board[4] == playerLetter and board[9] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[8] == playerLetter and board[3] == playerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[8] == playerLetter and board[1] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if (board[2] == playerLetter and board[6] == playerLetter) and possibleMoves.isSpaceFree(board,3):
        return 3;
    if (board[6] == playerLetter and board[8] == playerLetter) and possibleMoves.isSpaceFree(board,9):
        return 9;
    if (board[4] == playerLetter and board[8] == playerLetter) and possibleMoves.isSpaceFree(board,7):
        return 7;
    if(board[2] == playerLetter and board[4] == playerLetter) and possibleMoves.isSpaceFree(board,1):
        return 1;
        # Try to take one of the corners, if they are free.
    move = possibleMoves.chooseRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move
        # Move on one of the sides if nothing else
    return possibleMoves.chooseRandomMove(board, [2, 4, 6, 8])
