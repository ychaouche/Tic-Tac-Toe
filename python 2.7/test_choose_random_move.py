import moves
import boardlib
import unittest

class TestChooseRandomMove(unittest.TestCase):
    """ Test class for function moves.choose_random_move """

    def test_choose_random_move(self):
        """  Corners unavailable """

        b = boardlib.BoardLib(3)
        b.board[(0,0)] = 'X'
        b.board[(0,2)] = 'X'
        b.board[(2,0)] = 'X'
        b.board[(2,2)] = 'X'
        actual = moves.choose_random_move(b, [ (0,0), (0,2), (2,0), (2,2) ])
        expected = None
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex2(self):
        """  Center available """

        b = boardlib.BoardLib(3)
        actual = moves.choose_random_move(b, [(1,1)])
        expected = (1,1)
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex3(self):
        """  Sides unavailable """

        b = boardlib.BoardLib(3)
        b.board[(0,1)] = 'X'
        b.board[(1,0)] = 'X'
        b.board[(1,2)] = 'X'
        b.board[(2,1)] = 'X'
        actual = moves.choose_random_move(b, [ (0,1), (1,0), (1,2), (2,1) ])
        expected = None
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
