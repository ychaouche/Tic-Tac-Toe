import move_maker
import unittest

class TestMakeMove(unittest.TestCase):
    """ Test class for function moves.make_move """

    def test_make_move(self):
        """ Checks if the list has been mutated correctly """

        mutateme = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):' ', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):'X'}
        actual = move_maker.make_move(mutateme, "X", (0,1))
        expected = 'X'
        self.assertEqual(expected, mutateme[(0,1)])

        
if __name__ == '__main__':
    unittest.main(exit=False)
