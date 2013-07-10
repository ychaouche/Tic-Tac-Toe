import moves
import unittest

class TestChooseRandomMove(unittest.TestCase):
    """ Test class for function moves.choose_random_move """

    def test_choose_random_move(self):
        """  Corners unavailable """

        board = ["X", " ", "O", " ", " ", " ", "O", " ", "X"]
        actual = moves.choose_random_move(board, [0,2,6,8])
        expected = None
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex2(self):
        """  Center available """

        board = [" ", " ", " ", "X", " ", " ", " ", " ", " "]
        actual = moves.choose_random_move(board, [4])
        expected = 4
        self.assertEqual(expected, actual)

    def test_choose_random_move_ex3(self):
        """  Sides unavailable """

        board = [" ", "X", " ", "O", " ", "X", " ", "O", " "]
        actual = moves.choose_random_move(board, [1,3,5,7])
        expected = None
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
