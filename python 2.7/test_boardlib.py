import boardlib
import unittest

class TestBoardLib(unittest.TestCase):
    """ Test class for function boardlib.BoardLib """

    def test_board(self):
        """  A Board object's row/column arguments must be equal in length. """

        b = boardlib.BoardLib(3)
        self.assertEquals(max(b.board)[0],max(b.board)[1])
        
if __name__ == '__main__':
    unittest.main(exit=False)
