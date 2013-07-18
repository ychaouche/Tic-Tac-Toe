import moves
import unittest

class TestIsSpaceFree(unittest.TestCase):
    """ Test class for function moves.is_space_free """

    def test_is_space_free(self):
        """Checks if the correct bool was returned"""

        board = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):' ', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):'X'}
        actual = moves.is_space_free(board,(0,1))
        expected = True
        self.assertEqual(expected, actual)

    def test_is_space_free_ex2(self):
        """Checks if the correct bool was returned"""

        board = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):' ', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):'X'}
        actual = moves.is_space_free(board,(0,2))
        expected = False
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
