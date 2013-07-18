import move_maker
import boardlib

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
    print(output)
    
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
    return (raw_input().lower().startswith('y'))

def play_one_game():
    the_game_board = boardlib.BoardLib(3)
    player_letter, computer_letter = players_choice()
    print( "X" + ' goes first.')
    game_is_playing = True
    ai = ("O" == player_letter)
    while game_is_playing: 
        if ai:
            #ai_make_move(...)
            move_maker.make_move(the_game_board.board, computer_letter, move_maker.get_computer_move(the_game_board.board, computer_letter))
        else:
            draw_game_board(the_game_board)
            #player_make_move(..)
            move_maker.make_move(the_game_board.board, player_letter, move_maker.get_player_move(the_game_board.board))
        ai = not ai
        if move_maker.is_winner(the_game_board.board, player_letter):
            draw_game_board(the_game_board)
            print('You win.')
            break
        if move_maker.is_winner(the_game_board.board, computer_letter):
            draw_game_board(the_game_board)
            print('You Lose.')
            break
        if move_maker.is_game_board_full(the_game_board.board):
            draw_game_board(the_game_board)
            print('The game is a tie.')
            break
        
print('Welcome to Jose\'s Unbeatable Tic Tac Toe!')
instructions()

while True:
    play_one_game()
    if not play_again():
        break
