import move_maker

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
    for k in range(len(board)):
        print('   |   |')
        print(' ' + str(board[k][0]) + ' | ' + str(board[k][1]) + ' | ' + str(board[k][2]))
        print('   |   |')
        if k < 2:
            print('-----------')

def players_choice():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = raw_input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def play_again():
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

print('Welcome to Jose\'s Unbeatable Tic Tac Toe!')
instructions()

while True:
    the_game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_letter, computer_letter = players_choice()
    print( "X" + ' goes first.')
    game_is_playing = True
    ai = ("O" == player_letter)
    while game_is_playing: 
        if ai:
            #ai_make_move(...)
            move_maker.make_move(the_game_board, computer_letter, move_maker.get_computer_move(the_game_board, computer_letter))
        else:
            draw_game_board(the_game_board)
            #player_make_move(..)
            move_maker.make_move(the_game_board, player_letter, move_maker.get_player_move(the_game_board))
        ai = not ai
        if move_maker.is_winner(the_game_board, player_letter):
            draw_game_board(the_game_board)
            print('You win.')
            break
        if move_maker.is_winner(the_game_board, computer_letter):
            draw_game_board(the_game_board)
            print('You Lose.')
            break
        if move_maker.is_game_board_full(the_game_board):
            draw_game_board(the_game_board)
            print('The game is a tie.')
            break

    if not play_again():
        break
