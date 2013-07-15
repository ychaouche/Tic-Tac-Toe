import moves

def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    if moves.is_space_free(board, [1,1]):
        return [1,1]
    for i in get_all_positions(board):
        board_copy = [list(board[0]), list(board[1]), list(board[2])]
        if moves.is_space_free(board_copy, i):
                make_move(board_copy, computer_letter, i)
                if is_winner(board_copy, computer_letter):
                    return i
    for i in get_all_positions(board):
        board_copy = [list(board[0]), list(board[1]), list(board[2])]
        if moves.is_space_free(board_copy, i):
                make_move(board_copy, player_letter, i)
                if is_winner(board_copy, player_letter):
                    return i
    for i in [ [1,0], [1, 2], [0, 0] ]:
        if i == [1,0]:
            counter_move = [ [0,1], [0,2], [2,1], [2,2] ]
        else:
            counter_move = [ [0,0], [0,1], [2,0], [2,1] ]
        for j in counter_move:
            if ((board[i[0]][i[1]] == player_letter) and (board[j[0]][j[1]] == player_letter) and
                (moves.is_space_free(board, [j[0], i[1]]))):
                return [ j[0], i[1] ]
    move = moves.choose_random_move(board, [ [0,0], [0,2], [2,0], [2,2] ])
    if move != None and moves.is_space_free(board, move):
        return move
    return moves.choose_random_move(board, [ [0,1], [1,0], [1,2], [2,1] ])

def is_winner(board, letter):
    #Across
    for x in board:
        if ((x[0] == letter) and (x[1] == letter) and (x[2] == letter)):
            return True
    #Down
    for x in range(len(board)):
        if ((board[0][x] == letter) and (board[1][x] == letter) and (board[2][x] == letter)):
            return True
    #Diagonal
    return ((board[0][0] == letter and board[1][1] == letter and board[2][2] == letter) or
            (board[0][2] == letter and board[1][1] == letter and board[2][0] == letter))

def make_move(board, letter, move):
    board[move[0]][move[1]] = letter

def get_all_positions(board):
    return [[x,y] for x in range(len(board)) for y in range(len(board[0]))]

def get_player_move(board):
    move = ' '
    while move not in get_all_positions(board):
        move = raw_input('What is your next move? (1-9)\n')
        try:
            if 0 < int(move) <= 3 and moves.is_space_free(board, [0,(int(move))-1]):
                move = [0,(int(move))-1]
            elif 3 < int(move) <= 6 and moves.is_space_free(board, [1,(int(move))-4]):
                move = [1,(int(move))-4]
            elif 6 < int(move) <= 9 and moves.is_space_free(board, [2,(int(move))-7]):
                move = [2,(int(move))-7]
            elif ((int(move) > 9) or (int(move) < 1)):
                move = ' '
        except ValueError:
            pass
    return move

def is_game_board_full(board):
    for i in range(len(board)):
        for j in range(3):
            if moves.is_space_free(board, [i,j]):
                return False
    return True
