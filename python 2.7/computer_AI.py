import moves



def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
# All Moves
            # Winning Top Row
    if (board[1] == computer_letter and board[2] == computer_letter) and moves.is_space_free(board,3):
        return 3;
    if (board[1] == computer_letter and board[3] == computer_letter) and moves.is_space_free(board,2):
        return 2;
    if (board[2] == computer_letter and board[3] == computer_letter) and moves.is_space_free(board,1):
        return 1;

            # Winning Second Row
    if (board[4] == computer_letter and board[5] == computer_letter) and moves.is_space_free(board,6):
        return 6;
    if (board[4] == computer_letter and board[6] == computer_letter) and moves.is_space_free(board,5):
        return 5;
    if (board[5] == computer_letter and board[6] == computer_letter) and moves.is_space_free(board,4):
        return 4;

        # Winning Third Row
    if (board[7] == computer_letter and board[8] == computer_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[7] == computer_letter and board[9] == computer_letter) and moves.is_space_free(board,8):
        return 8;
    if (board[8] == computer_letter and board[9] == computer_letter) and moves.is_space_free(board,7):
        return 7;

        # Winning First Column

    if (board[1] == computer_letter and board[4] == computer_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[1] == computer_letter and board[7] == computer_letter) and moves.is_space_free(board,4):
        return 4;
    if (board[4] == computer_letter and board[7] == computer_letter) and moves.is_space_free(board,1):
        return 1;

        # Winning Second Column
    if (board[2] == computer_letter and board[5] == computer_letter) and moves.is_space_free(board,8):
        return 8;
    if (board[2] == computer_letter and board[8] == computer_letter) and moves.is_space_free(board,5):
        return 5;
    if (board[5] == computer_letter and board[8] == computer_letter) and moves.is_space_free(board,2):
        return 2;

        # Winning Third Column
    if (board[3] == computer_letter and board[6] == computer_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[3] == computer_letter and board[9] == computer_letter) and moves.is_space_free(board,6):
        return 6;
    if (board[6] == computer_letter and board[9] == computer_letter) and moves.is_space_free(board,3):
        return 4;

        # Winning Left to Right Diagonal
    if (board[1] == computer_letter and board[5] == computer_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[1] == computer_letter and board[9] == computer_letter) and moves.is_space_free(board,5):
        return 5;
    if (board[5] == computer_letter and board[9] == computer_letter) and moves.is_space_free(board,1):
        return 1;

        # Winning Right to Left Diagonal
    if (board[3] == computer_letter and board[5] == computer_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[3] == computer_letter and board[7] == computer_letter) and moves.is_space_free(board,5):
        return 5;
    if (board[5] == computer_letter and board[7] == computer_letter) and moves.is_space_free(board,3):
        return 3;

            # Top Row Horizontal Blocking
    if (board[1] == player_letter and board[2] == player_letter) and moves.is_space_free(board,3):
        return 3;
    if (board[2] == player_letter and board[3] == player_letter) and moves.is_space_free(board,1):
        return 1;
    if (board[1] == player_letter and board[3] == player_letter) and moves.is_space_free(board,2):
        return 2;

            # Second Row Horizontal Blocking
    if (board[4] == player_letter and board[5] == player_letter) and moves.is_space_free(board,6):
        return 6;
    if (board[5] == player_letter and board[6] == player_letter) and moves.is_space_free(board,4):
        return 4;
    if (board[4] == player_letter and board[6] == player_letter) and moves.is_space_free(board,5):
        return 5;

            # Third Row Horizontal Blocking
    if (board[7] == player_letter and board[8] == player_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[8] == player_letter and board[9] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[7] == player_letter and board[9] == player_letter) and moves.is_space_free(board,8):
        return 8;

            # First Column Vertical Blocking
    if (board[1] == player_letter and board[4] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[4] == player_letter and board[7] == player_letter) and moves.is_space_free(board,1):
        return 1;
    if (board[1] == player_letter and board[7] == player_letter) and moves.is_space_free(board,4):
        return 4;

            # Second Column Vertical Blocking
    if (board[2] == player_letter and board[5] == player_letter) and moves.is_space_free(board,8):
        return 8;
    if (board[5] == player_letter and board[8] == player_letter) and moves.is_space_free(board,2):
        return 2;
    if (board[2] == player_letter and board[8] == player_letter) and moves.is_space_free(board,5):
        return 5;

            # Third Column Vertical Blocking
    if (board[3] == player_letter and board[6] == player_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[3] == player_letter and board[9] == player_letter) and moves.is_space_free(board,6):
        return 6;
    if (board[6] == player_letter and board[9] == player_letter) and moves.is_space_free(board,3):
        return 3;

            # Left to Right Diagonal
    if(board[1] == player_letter and board[5] == player_letter) and moves.is_space_free(board,9):
        return 9;
    if(board[1] == player_letter and board[9] == player_letter) and moves.is_space_free(board,5):
        return 5;
    if(board[5] == player_letter and board[9] == player_letter) and moves.is_space_free(board,1):
        return 1;

            # Right to Left Diagonal
    if (board[3] == player_letter and board[5] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[3] == player_letter and board[7] == player_letter) and moves.is_space_free(board,5):
        return 5;
    if (board[5] == player_letter and board[7] == player_letter) and moves.is_space_free(board,3):
        return 3;

        # Take Center if it's Free
    if moves.is_space_free(board, 5):
        return 5

        # Counteract if they form a diagonal with PL in 5 and in 9
    if (board[5] == player_letter and board[1] == computer_letter and board[9] == player_letter) and moves.is_space_free(board,6):
        return 6;
    if (board[5] == player_letter and board[1] == computer_letter and board[9] == player_letter) and moves.is_space_free(board,8):
        return 8;
    if (board[5] == player_letter and board[1] == computer_letter and board[9] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[5] == player_letter and board[1] == computer_letter and board[9] == player_letter) and moves.is_space_free(board,3):
        return 3;

        # Counteract if they form a diagonal with PL in 5 and in 1
    if (board[5] == player_letter and board[9] == computer_letter and board[1] == player_letter) and moves.is_space_free(board,2):
        return 2;
    if (board[5] == player_letter and board[9] == computer_letter and board[1] == player_letter) and moves.is_space_free(board,4):
        return 4;
    if (board[5] == player_letter and board[9] == computer_letter and board[1] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[5] == player_letter and board[9] == computer_letter and board[1] == player_letter) and moves.is_space_free(board,3):
        return 3;

        # Counteract if they form a diagonal with PL in 5 and in 7
    if (board[5] == player_letter and board[3] == computer_letter and board[7] == player_letter) and moves.is_space_free(board,1):
        return 1;
    if (board[5] == player_letter and board[3] == computer_letter and board[7] == player_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[5] == player_letter and board[3] == computer_letter and board[7] == player_letter) and moves.is_space_free(board,4):
        return 4;
    if (board[5] == player_letter and board[3] == computer_letter and board[7] == player_letter) and moves.is_space_free(board,8):
        return 8;

        # Counteract if a diagonal with CL in 5 and PL in 1 & 9
    if (board[1] == player_letter and board[5] == computer_letter and board[9] == player_letter) and moves.is_space_free(board,2):
        return 2;
    if (board[1] == player_letter and board[5] == computer_letter and board[9] == player_letter) and moves.is_space_free(board,8):
        return 8;


        # Counteract if diagonal with CL in 5 and PL in 3 & 7
    if (board[3] == player_letter and board[5] == computer_letter and board[7] == player_letter) and moves.is_space_free(board,2):
        return 2;
    if (board[3] == player_letter and board[5] == computer_letter and board[7] == player_letter) and moves.is_space_free(board,8):
        return 8;


    if (board[2] == player_letter and board[9] == player_letter) and moves.is_space_free(board,3):
        return 3;
    if (board[2] == player_letter and board[7] == player_letter) and moves.is_space_free(board,1):
        return 1;
    if (board[6] == player_letter and board[1] == player_letter) and moves.is_space_free(board,3):
        return 3;
    if (board[6] == player_letter and board[7] == player_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[4] == player_letter and board[3] == player_letter) and moves.is_space_free(board,1):
        return 1;
    if (board[4] == player_letter and board[9] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[8] == player_letter and board[3] == player_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[8] == player_letter and board[1] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if (board[2] == player_letter and board[6] == player_letter) and moves.is_space_free(board,3):
        return 3;
    if (board[6] == player_letter and board[8] == player_letter) and moves.is_space_free(board,9):
        return 9;
    if (board[4] == player_letter and board[8] == player_letter) and moves.is_space_free(board,7):
        return 7;
    if(board[2] == player_letter and board[4] == player_letter) and moves.is_space_free(board,1):
        return 1;
        # Try to take one of the corners, if they are free.
    move = moves.choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
        # Move on one of the sides if nothing else
    return moves.choose_random_move(board, [2, 4, 6, 8])
