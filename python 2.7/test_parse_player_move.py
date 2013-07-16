import unittest
import move_maker

class TestParsePlayerMove(unittest.TestCase):
    """ Test class for function move_maker.get_player_move """

    def test_parse_player_move(self):
        """  return player's move """

        board = [['X', ' ', 'O'], [' ', ' ', ' '], ['O', ' ', 'X']]
        actual = move_maker.parse_player_move('4', board)
        expected = [1, 0]
        self.assertEqual(expected, actual)

    def test_parse_player_move_ex2(self):
        """  nonvalid string input returns same input """

        board = [['X', ' ', 'O'], [' ', ' ', ' '], ['O', ' ', 'X']]
        actual = move_maker.parse_player_move('jjjj', board)
        expected = 'jjjj'
        self.assertEqual(expected, actual)


    def test_parse_player_move_ex3(self):
        """  nonvalid string input returns same input """

        board = [['X', ' ', 'O'], [' ', ' ', ' '], ['O', ' ', 'X']]
        actual = move_maker.parse_player_move('25', board)
        expected = ' '
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
