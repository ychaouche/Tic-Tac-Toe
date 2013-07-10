import computer_ai
import moves

# Tic Tac Toe
import random
def instructions():
    print("""
You will make your move by entering a number, 1 - 9.
The number will correspond to the board position as shown below

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Have fun, and good luck.

"""
    )
def draw_game_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def players_choice():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = raw_input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not moves.is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = raw_input()
    return int(move)

def is_game_board_full(board):
    for i in range(1, 10):
        if moves.is_space_free(board, i):
            return False
    return True

def play_again():
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

print('Welcome to Jose\'s Unbeatable Tic Tac Toe!')
instructions()

while True:
    the_game_board = [' '] * 10
    player_letter, computer_letter = players_choice()
    turn = "X"
    print( turn + ' goes first.')
    game_is_playing = True
    while game_is_playing:
        if turn == player_letter:
            draw_game_board(the_game_board)
            move = get_player_move(the_game_board)
            moves.make_move(the_game_board, player_letter, move)
            if moves.is_winner(the_game_board, player_letter):
                draw_game_board(the_game_board)
                print('You win.')
                game_is_playing = False
            else:
                if is_game_board_full(the_game_board):
                    draw_game_board(the_game_board)
                    print('The game is a tie.')
                    game_is_playing = False
                else:
                    turn = computer_letter
        else:
            move = computer_ai.get_computer_move(the_game_board, computer_letter)
            moves.make_move(the_game_board, computer_letter, move)
            if moves.is_winner(the_game_board, computer_letter):
                draw_game_board(the_game_board)
                print('You Lose.')
                game_is_playing = False
            else:
                if is_game_board_full(the_game_board):
                    draw_game_board(the_game_board)
                    print('The game is a tie!')
                    game_is_playing = False
                else:
                    turn = player_letter
    if not play_again():
        break
