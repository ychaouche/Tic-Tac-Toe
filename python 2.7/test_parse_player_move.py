import unittest
import move_maker

class TestParsePlayerMove(unittest.TestCase):
    """ Test class for function move_maker.get_player_move """

    def test_parse_player_move(self):
        """  return player's move """

        board = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):' ', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):'X'}
        actual = move_maker.parse_player_move('4', board)
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_parse_player_move_ex2(self):
        """  nonvalid string input returns same input """

        board = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):' ', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):'X'}
        actual = move_maker.parse_player_move('jjjj', board)
        expected = 'jjjj'
        self.assertEqual(expected, actual)


    def test_parse_player_move_ex3(self):
        """  nonvalid string input returns same input """

        board = {(0, 0):'X', (0, 1):' ', (0, 2):'O', (1, 0):' ', (1, 1):' ', (1, 2):' ', (2, 0):'O', (2, 1):' ', (2, 2):'X'}
        actual = move_maker.parse_player_move('25', board)
        expected = ' '
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
