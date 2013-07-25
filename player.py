import pprint

class Player:
    def __init__(self,game):
        self.game = game
        
    def set_playing_letter(self,letter):
        self.playing_letter = letter

    def wins(self):
        """
        Returns true if the player wins the game
        """
        return self.game.board.is_winning(self.playing_letter)

    def get_winning_move(self):
        return self.game.board.get_winning_move(self.playing_letter)

    def display_winning_message(self):
        """
        """
        print self.player_type,"won"
    
class HumanPlayer(Player):
    def __init__(self,game):
        Player.__init__(self,game)
        self.player_type = "You"
            
            
    def play(self):
        print "[DEBUG] show board in HumanPlayer.play()"
        self.game.board.show()
        move = ' '
        while not (move in sorted(self.game.board._board) and self.game.board.is_free(move)):
            square_number = raw_input('What is your next move? (1-9)\n')
            if not square_number.isdigit():
                continue
            square_number = int(square_number)
            move          = self.game.board.square_to_move(square_number)
        self.game.board.put_mark(self.playing_letter,move)
        
class AIPlayer(Player):
    def __init__(self,game):
        Player.__init__(self,game)
        self.player_type = "Computer"
        
    def play(self):
        move_functions = [
            self.get_1_1_move,                                                
            self.get_winning_move,
            self.game.human_player.get_winning_move,
            self.get_counter_move,
            self.get_random_move_1,
            self.get_random_move_2
            ]
        for function in move_functions:
            #print '[DEBUG] trying function',function.__name__
            move = function()
            #print "[DEBUG] got move %s (%s)" % (self.game.board.move_to_square(move),move)
            if move :
                self.game.board.put_mark(self.playing_letter,move)
                break
            
    def get_1_1_move(self):
        if self.game.board.is_free((1,1)):
            return ((1,1))
        
    def get_counter_move(self):
        board        = self.game.board
        owner        = board.owner
        human_player = self.game.human_player
        ai_player    = self.game.ai_player

        for i in [ (1,0), (1, 2), (0, 0) ]:
            if i == (1,0):
                counter_moves = [ (0,1), (0,2), (2,1), (2,2) ]
            else:
                counter_moves = [ (0,0), (0,1), (2,0), (2,1) ]

            if not owner(i) == human_player:
                continue
            
            for j in counter_moves:
                position = (j[0], i[1])
                if (owner(j) == human_player) and (board.is_free(position)):
                    return (j[0], i[1])

    def get_random_move_1(self):
        return self.get_random_move([ (0,0), (0,2), (2,0), (2,2) ])

    def get_random_move_2(self):
        return self.get_random_move([ (0,1), (1,0), (1,2), (2,1) ])
        
    def get_random_move(self,moves):
        return self.game.board.get_random_valid_move(moves)

        

    
