from board import Board
from player import HumanPlayer,AIPlayer

# Tic Tac Toe
import random

class Game:
    def __init__(self,board_size=3):
        self.board_size = board_size
        self.reset()

    def reset(self):
        self.board = Board(self,self.board_size)
        
    def intro(self):
        print('Welcome to Jose\'s Unbeatable Tic Tac Toe!')
        print """

        Use your keypad as if it were the board
        
        7 | 8 | 9
        ---------
        4 | 5 | 6
        ---------
        1 | 2 | 3
        
        Have fun, and good luck.
        """

    def letter_choice(self):
        letter = None
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = raw_input().upper()

        return letter

    def create_players(self):
        print( "X goes first.")
        self.human_player = HumanPlayer(game = self)
        self.ai_player    = AIPlayer(game = self)
        self.human_player.set_playing_letter(self.letter_choice())
        self.ai_player.set_playing_letter({"X":"O","O":"X"}.get(self.human_player.playing_letter))
        print "[DEBUG] ai_player plays as",self.ai_player.playing_letter
        print "[DEBUG] human player plays as",self.human_player.playing_letter
        # We need an ordered list for the mainloop
        return self.human_first() and [self.human_player,self.ai_player] or [self.ai_player,self.human_player]

    def human_first(self):
        return self.human_player.playing_letter == "X"
        
    def play_again(self):
        print('Do you want to play again? (yes or no)')
        return (raw_input().lower().startswith('y'))

    def mainloop(self):
        players         = self.create_players()
        game_is_playing = True
        while game_is_playing:
            for player in players :
                player.play()
                #self.board.show()
                if player.wins():
                    print "[DEBUG] show board after win"
                    self.board.show()                    
                    player.display_winning_message()
                    # gets out of the while loop
                    game_is_playing = False
                    # gets out of the foor loop
                    break
                elif self.board.is_full():
                    self.board.show()
                    print('The game is a tie.')
                    # gets out of the while loop
                    game_is_playing = False
                    # gets out of the foor loop
                    break

        return self.play_again()

    
def main():
    game = Game(board_size=3)
    game.intro()
    while(game.mainloop()):
        game.reset()
        print "Let's go for another round !"

if __name__ == "__main__":
    main()
