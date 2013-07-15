import moves
import unittest

class TestChooseRandomMove(unittest.TestCase):
    """ Test class for function moves.choose_random_move """

    def test_choose_random_move(self):
        """  Corners unavailable """

        board = [['X', ' ', 'O'], [' ', ' ', ' '], ['O', ' ', 'X']]
        actual = moves.choose_random_move(board, [ [0,0], [0,2], [2,0], [2,2] ])
        expected = None
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex2(self):
        """  Center available """

        board = [[' ', ' ', ' '], ['X', ' ', ' '], [' ', ' ', ' ']]
        actual = moves.choose_random_move(board, [[1,0]])
        expected = None
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex3(self):
        """  Sides unavailable """

        board = [[' ', 'X', ' '], ['O', ' ', 'X'], [' ', 'O', ' ']]
        actual = moves.choose_random_move(board, [ [0,1], [1,0], [1,2], [2,1] ])
        expected = None
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
