import moves
import unittest

class TestChooseRandomMove(unittest.TestCase):
    """ Test class for function moves.choose_random_move """

    def test_choose_random_move(self):
        """  Corners unavailable """

        board = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):' ', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):'X'}
        actual = moves.choose_random_move(board, [ (0,0), (0,2), (2,0), (2,2) ])
        expected = None
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex2(self):
        """  Center available """

        board = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):'X', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):' '}
        actual = moves.choose_random_move(board, [(1,1)])
        expected = (1,1)
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex3(self):
        """  Sides unavailable """

        board = {(0, 0):' ', (0, 1):'X', (0, 2):' ', (1, 0):'X', (1, 1):' ', (1, 2):'O', (2, 0):' ', (2, 1):'O', (2, 2):' '}
        actual = moves.choose_random_move(board, [ (0,1), (1,0), (1,2), (2,1) ])
        expected = None
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
