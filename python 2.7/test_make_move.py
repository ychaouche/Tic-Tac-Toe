import move_maker
import unittest

class TestMakeMove(unittest.TestCase):
    """ Test class for function moves.make_move """

    def test_make_move(self):
        """ Checks if the list has been mutated correctly """

        mutateme = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        actual = move_maker.make_move(mutateme, "X", [0,1])
        expected = [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(expected, mutateme)

        
if __name__ == '__main__':
    unittest.main(exit=False)
