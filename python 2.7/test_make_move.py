import moves
import unittest

class TestMakeMove(unittest.TestCase):
    """ Test class for function moves.make_move """

    def test_make_move(self):
        """ Checks if the list has been mutated correctly """

        mutateme = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        actual = moves.make_move(mutateme, "X", 1)
        expected = [" ", "X", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(expected, mutateme)

        
if __name__ == '__main__':
    unittest.main(exit=False)
