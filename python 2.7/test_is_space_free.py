import moves
import unittest

class TestIsSpaceFree(unittest.TestCase):
    """ Test class for function moves.is_space_free """

    def test_is_space_free(self):
        """Checks if the correct bool was returned"""

        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        actual = moves.is_space_free(board,[0,1])
        expected = True
        self.assertEqual(expected, actual)

    def test_is_space_free_ex2(self):
        """Checks if the correct bool was returned"""

        board = [[' ', 'O', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        actual = moves.is_space_free(board,[0,1])
        expected = False
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
