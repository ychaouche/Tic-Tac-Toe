import sys
sys.path.append("..")
from board import Board
from game import Game
import unittest

class TestBoardLib(unittest.TestCase):
    """ Test class for function boardlib.BoardLib """
    def test_size(self):
        """  A Board object's row/column arguments must be equal in length. """
        b = Board(Game(),3)
        max_rows    = max(b._board,key=lambda d:d[1])[1]
        max_columns = max(b._board,key=lambda d:d[0])[0]
        self.assertEqual(max_rows,max_columns)

    def test_is_free(self):
        """ tests is_free """
        b = Board(Game(),3)
        square = 3
        b.put_mark("x",square=square)
        actual = b.is_free(square=square)
        expected = False
        self.assertEqual(expected, actual)

    def test_put_mark(self):
        """ tests put_mark """
        square = 3
        b      = Board(Game(),3)
        c      = Board(Game(),3)
        b.put_mark("X",square=square)
        c.put_mark("X",square=square)
        actual   = c.get(square=square)
        expected = b.get(square=square)
        self.assertEqual(expected, actual)

    def test_is_full(self):
        """ tests is_full """
        b = Board(Game(),3)
        for move in b._board:
            b.put_mark("X",move)
        
        actual   = b.is_full()
        expected = True
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
