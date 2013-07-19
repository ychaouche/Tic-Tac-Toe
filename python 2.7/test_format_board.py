import unittest
import move_maker
import boardlib

class TestFormatBoard(unittest.TestCase):
    """ Test class for function commandlineTTT.draw_game_board """

    def test_format_board(self):
        """ return gameboard in a string """

        b =  boardlib.BoardLib(3)
        actual = move_maker.format_board(b)
        expected = '\n   |   |\n   |   |  \n   |   |\n----------- \n   |   |\n   |   |  \n   |   |\n----------- \n   |   |\n   |   |  \n   |   |\n'
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
