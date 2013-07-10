import moves

def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    for i in range(1,10):
        board_copy = list(board)
        if moves.is_space_free(board_copy, i):
            moves.make_move(board_copy, computer_letter, i)
            if moves.is_winner(board_copy, computer_letter):
                return i  
    for i in range(1,10):
        board_copy = list(board)
        if moves.is_space_free(board_copy, i):
            moves.make_move(board_copy, player_letter, i)
            if moves.is_winner(board_copy, player_letter):
                return i
    for i in [4, 6]:
        trap = {1:3, 2:1, 3:1, 7:9, 8:7, 9:7}
        for x in trap:
            if board[i] == player_letter and board[x] == player_letter and moves.is_space_free(board, trap[x]):
                return trap[x]
    if moves.is_space_free(board, 5):
        return 5
    move = moves.choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    return moves.choose_random_move(board, [2, 4, 6, 8])
