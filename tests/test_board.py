import boardlib
import unittest

class TestBoardLib(unittest.TestCase):
    """ Test class for function boardlib.BoardLib """

    def test_board(self):
        """  A Board object's row/column arguments must be equal in length. """

        b = boardlib.BoardLib(3)
        self.assertEqual(max(b.board)[0],max(b.board)[1])

    def test_board_ex2(self):
        """ tests is_space_free """

        b = boardlib.BoardLib(3)
        b.board[(0,2)] = "X"
        actual = b.is_space_free((0,2))
        expected = False
        self.assertEqual(expected, actual)

    def test_board_ex3(self):
        """ tests make_move """

        b = boardlib.BoardLib(3)
        b.board[(0,2)] = "X"
        c = boardlib.BoardLib(3)
        c.make_move('X', (0,2))
        actual = c.board[(0,2)]
        expected = b.board[(0,2)]
        self.assertEqual(expected, actual)

    def test_board_ex4(self):
        """ tests make_move """

        b = boardlib.BoardLib(3)
        for w in b.board:
            b.board[w] = "X"
        actual = b.is_game_board_full()
        expected = True
        self.assertEqual(expected, actual)

    
        
if __name__ == '__main__':
    unittest.main(exit=False)
