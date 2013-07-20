import unittest
import move_maker
import boardlib

class TestWins(unittest.TestCase):
    """ Test class for function move_maker.wins """

    def test_wins(self):
        """  returns winning move """

        b = boardlib.BoardLib(3)
        b.make_move('X', (0,0))
        b.make_move('X', (0,1))
        actual = move_maker.wins(b, 'X')
        expected = (0,2)
        self.assertEqual(expected, actual)

                
if __name__ == '__main__':
    unittest.main(exit=False)
