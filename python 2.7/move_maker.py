import moves
import copy

def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    if board.is_space_free((1,1)):
        return (1,1)
    for i in sorted(board.board):
        board_copy = copy.deepcopy(board)
        if board_copy.is_space_free(i):
                board_copy.make_move(computer_letter, i)
                if is_winner(board_copy, computer_letter):
                    return i
    for i in sorted(board.board):
        board_copy = copy.deepcopy(board)
        if board_copy.is_space_free(i):
                board_copy.make_move(player_letter, i)
                if is_winner(board_copy, player_letter):
                    return i
    for i in [ (1,0), (1, 2), (0, 0) ]:
        if i == (1,0):
            counter_move = [ (0,1), (0,2), (2,1), (2,2) ]
        else:
            counter_move = [ (0,0), (0,1), (2,0), (2,1) ]
        for j in counter_move:
            if ((board.board[i] == player_letter) and (board.board[j] == player_letter) and
                (board.is_space_free((j[0], i[1])))):
                return (j[0], i[1])
    move = moves.choose_random_move(board, [ (0,0), (0,2), (2,0), (2,2) ])
    if move != None and board.is_space_free(move):
        return move
    return moves.choose_random_move(board, [ (0,1), (1,0), (1,2), (2,1) ])

def is_winner(board, letter):
    #Across
    for x in range((max(board.board)[0]+1)):
        if ((board.board[(x,0)] == letter) and (board.board[(x,1)] == letter) and (board.board[(x,2)] == letter)):
            return True
    #Down
    for x in range((max(board.board)[0]+1)):
        if ((board.board[(0,x)] == letter) and (board.board[(1,x)] == letter) and (board.board[(2,x)] == letter)):
            return True
    #Diagonal
    return ((board.board[(0,0)] == letter and board.board[(1,1)] == letter and board.board[(2,2)] == letter) or
            (board.board[(0,2)] == letter and board.board[(1,1)] == letter and board.board[(2,0)] == letter))

def parse_player_move(move, board):
    try:
        if 0 < int(move) <= 3 and board.is_space_free((0,(int(move))-1)):
            move = (0,(int(move))-1)
        elif 3 < int(move) <= 6 and board.is_space_free((1,(int(move))-4)):
            move = (1,(int(move))-4)
        elif 6 < int(move) <= 9 and board.is_space_free((2,(int(move))-7)):
            move = (2,(int(move))-7)
        elif ((int(move) > 9) or (int(move) < 1) or (move != ' ')):
            move = ' '
    except ValueError:
        pass
    return move

def get_player_move(board):
    move = ' '
    while move not in sorted(board.board):
        move = raw_input('What is your next move? (1-9)\n')
        move = parse_player_move(move, board)
    return move

def format_board(board):
    output = ''
    for r in range(board.size):
        if 1 <= r < (board.size):
            output += '----------- '
        output += '\n   |   |\n'
        for c in range(board.size):
            output += ' ' + board.board[r,c]
            if c < (board.size-1):
                output += ' |'
        output += '\n   |   |\n'
    return (output)
