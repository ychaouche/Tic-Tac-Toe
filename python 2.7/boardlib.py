class BoardLib:
    def __init__(self, size):
        self.size = size
        self.board = {(x,y) : (' ') for x in range(size) for y in range(size)}
        
    def make_move(self, letter, move):
        self.board[move] = letter
 
    def is_game_board_full(self):
        for i in self.board:
            if ' ' in self.board[i]:
                return False
        return True
 
    def is_space_free(self, move):
        return self.board[move] == ' '
