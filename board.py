
import random
import copy

class Board:
    def __init__(self,game, size):
        self.game   = game
        self.size   = size
        self._board = {(x,y) : (' ') for x in range(size) for y in range(size)}

    def put_mark(self, letter, move=None,square=None):
        if square :
            move = self.square_to_move(square)
        else :
            square = self.move_to_square(move)
        #print "[DEBUG] put_mark %s on square %s (%s)" % (letter,square,move)
        self._board[move] = letter

    def is_full(self):
        for i in sorted(self._board):
            if ' ' in self._board[i]:
                return False
        return True

    def is_free(self, move):
        return self._board[move] == ' '

    def show(self):
        for row in xrange(self.size,0,-1):
            line = []
            for col in xrange(self.size):
                line += self._board[(row-1,col)]
            print "     |     |     "
            print "  %s  |  %s  |  %s  " % (line[0],line[1],line[2])
            print "     |     |     "
            if row-1 != 0:
                print "-----|-----|-----"

    def get(self,position):
        return self._board[position]

    def get_owner(self,position):
        mark = self.get(position)
        if mark == self.game.human_player.playing_letter :
            return self.game.human_player
        elif mark == self.game.ai_player :
            return self.game.ai_player

    def get_random_valid_move(self,moves):
        possible_moves = [move for move in moves if self.is_free(move)]
        return possible_moves and random.choice(possible_moves) or None

    def square_to_move(self,square):
        """
           x
           ^              KEYPAD                        BOARD
           .    +-------+-------+-------+     +-------+-------+-------+
           .    |       |       |       |     |       |       |       |
           .    |   7   |   8   |   9   |     | (2,0) | (2,1) | (2,2) |
         2 _    |       |       |       |     |       |       |       |
           .    +-------+-------+-------+     +-------+-------+-------+
           .    |       |       |       |     |       |       |       |
       X 1 _    |   4   |   5   |   6   | --> | (1,0) | (1,1) | (1,2) |
           .    |       |       |       |     |       |       |       |
           .    +-------+-------+-------+     +-------+-------+-------+
           .    |       |       |       |     |       |       |       |
         0 _    |   1   |   2   |   3   |     | (0,0) | (0,1) | (0,2) |
           .    |       |       |       |     |       |       |       |
           .    +-------+-------+-------+     +-------+-------+-------+
           +--------0-------1-------2-------------0-------1-------2----------> y
                                           Y
        """

        if not 1 <= square <= self.size*self.size :
            #print "[DEBUG] square_to_move(%s) is out of range" % (square)
            return
        y = (square - 1) % self.size
        x = (square - 1) / self.size
        return (x,y)

    def move_to_square(self,move):
        """

           x
           ^            BOARD                         KEYPAD
           .  +-------+-------+-------+      +-------+-------+-------+
           .  |       |       |       |      |       |       |       |
           .  | (2,0) | (2,1) | (2,2) |      |   7   |   8   |   9   |
         2 _  |       |       |       |      |       |       |       |
           .  +-------+-------+-------+      +-------+-------+-------+
           .  |       |       |       |      |       |       |       |
       X 1 _  | (1,0) | (1,1) | (1,2) | -->  |   4   |   5   |   6   |
           .  |       |       |       |      |       |       |       |
           .  +-------+-------+-------+      +-------+-------+-------+
           .  |       |       |       |      |       |       |       |
         0 _  | (0,0) | (0,1) | (0,2) |      |   1   |   2   |   3   |
           .  |       |       |       |      |       |       |       |
           .  +-------+-------+-------+      +-------+-------+-------+
           +------0-------1-------2--------------0-------1-------2----------> y
                                           Y
        """
        if not move :
            return
        x,y = move
        if 0 <= x <= self.size and 0 <= y <= self.size :
            return (x*self.size) + y + 1

    def is_winning(self,mark):
        #Across

        for x in range((max(self._board)[0]+1)):
            if ((self._board[(x,0)] == mark) and (self._board[(x,1)] == mark) and (self._board[(x,2)] == mark)):
                #print "[DEBUG] HORIZONTAL",mark
                return True
        #Down
        for x in range((max(self._board)[0]+1)):
            if ((self._board[(0,x)] == mark) and (self._board[(1,x)] == mark) and (self._board[(2,x)] == mark)):
                #print "[DEBUG] VERTICAL",mark
                return True
        #Diagonal
        if ((self._board[(0,0)] == mark and self._board[(1,1)] == mark and self._board[(2,2)] == mark) or (self._board[(0,2)] == mark and self._board[(1,1)] == mark and self._board[(2,0)] == mark)) :
            #print "[DEBUG] DIAGONAL",mark
            return True


    def get_winning_move(self, mark):
        #print "[DEBUG] get_winning_move for mark",mark
        backup_board = copy.deepcopy(self._board)
        move         = None
        for i in sorted(backup_board):
            #print "[DEBUG] board before restoring backup"
            #self.show()
            #raw_input()
            self._board = copy.deepcopy(backup_board)
            #print "[DEBUG] board after restoring backup"
            #self.show()
            #raw_input()
            if not self.is_free(i):
               # print '[DEBUG] square %s is not free' % (self.move_to_square(i))
                continue
            self.put_mark(mark, i)
            if self.is_winning(mark):
                #print '[DEBUG] square %s is a winning move' % (self.move_to_square(i))
                move = i
                break

        self._board = backup_board
        return move
