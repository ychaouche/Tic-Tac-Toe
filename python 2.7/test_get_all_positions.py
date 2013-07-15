import unittest
import move_maker

class TestGetAllPositions(unittest.TestCase):
    """ Test class for function move_maker.get_all_positions """

    def test_get_all_positions(self):
        """ 4x4 grid """

        board = [ [" ", " "," ", " "],
                  [" ", " "," ", " "],
                  [" ", " "," ", " "],
                  [" ", " "," ", " "]
                ]
        actual = move_maker.get_all_positions(board)
        expected = [[0, 0], [0, 1], [0, 2], [0, 3],
                    [1, 0], [1, 1], [1, 2], [1, 3],
                    [2, 0], [2, 1], [2, 2], [2, 3],
                    [3, 0], [3, 1], [3, 2], [3, 3]
                   ]
        self.assertEqual(expected, actual)

    def test_get_all_positions_ex2(self):
        """ 3x3 grid """

        board = [ [" ", " "," "],
                  [" ", " "," "],
                  [" ", " "," "]
                ]
        actual = move_maker.get_all_positions(board)
        expected = [[0, 0], [0, 1], [0, 2],
                    [1, 0], [1, 1], [1, 2],
                    [2, 0], [2, 1], [2, 2],
                   ]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
