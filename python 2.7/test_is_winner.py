import unittest
import move_maker
import boardlib

class TestIsWinner(unittest.TestCase):
    """ Test class for function move_maker.is_winner """

    def test_is_winner(self):
        """ return bool """

        b = boardlib.BoardLib(3)
        actual = move_maker.is_winner(b, "X")
        expected = False
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
