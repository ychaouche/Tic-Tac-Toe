import sys
sys.path.append("..")
from board import Board
from game import Game
import unittest
 
class TestBoardLib(unittest.TestCase):
    """ Test class for function boardlib.BoardLib """

    def test_size(self):
        """  A Board object's row/column arguments must be equal in length. """
        b           = Game(board_size=3).board
        max_rows    = max(b._board,key=lambda d:d[0])[0]        
        max_columns = max(b._board,key=lambda d:d[1])[1]
        self.assertEqual(max_rows,max_columns)

    def test_is_free(self):
        """ tests is_free """
        b = Game(board_size=3).board        
        square = 3
        b.put_mark("x",square=square)
        actual = b.is_free(square=square)
        expected = False
        self.assertEqual(expected, actual)

    def test_put_mark(self):
        """ tests put_mark """
        square = 3
        b = Game(board_size=3).board
        c = Game(board_size=3).board                
        b.put_mark("X",square=square)
        c.put_mark("X",square=square)
        actual   = c.get(square=square)
        expected = b.get(square=square)
        self.assertEqual(expected, actual)

    def test_is_full(self):
        """ tests is_full """
        b      = Board(Game(),3)
        for move in b._board:
            b.put_mark("X",move)
        
        actual   = b.is_full()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_winning_horizonal(self):
        """
        """
        game = Game()
        game.board.put_mark("X",square=1)
        game.board.put_mark("X",square=2)
        game.board.put_mark("X",square=3)
        self.assertEqual(game.board.is_winning("X"),True)
        game.board.game.reset()
        self.assertEqual(game.board.is_free(square=1),True)
        self.assertEqual(game.board.is_free(square=2),True)
        self.assertEqual(game.board.is_free(square=3),True)
        game.board.put_mark("X",square=4)
        game.board.put_mark("X",square=5)
        game.board.put_mark("X",square=6)
        self.assertEqual(game.board.is_winning("X"),True)        
        game.board.game.reset()
        self.assertEqual(game.board.is_free(square=4),True)
        self.assertEqual(game.board.is_free(square=5),True)
        self.assertEqual(game.board.is_free(square=6),True)
        game.board.put_mark("X",square=7)
        game.board.put_mark("X",square=8)
        game.board.put_mark("X",square=9)
        self.assertEqual(game.board.is_winning("X"),True)        
        
if __name__ == '__main__':
    unittest.main(exit=False)
