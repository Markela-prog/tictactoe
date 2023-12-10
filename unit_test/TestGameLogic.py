import unittest
from game_logic import initialize_board, check_win

class TestGameLogic(unittest.TestCase):

    def test_initialize_board(self):
        sizes = [3, 4, 5]
        for size in sizes:
            with self.subTest(size=size):
                board = initialize_board(size)
                self.assertEqual(len(board), size)
                for row in board:
                    self.assertEqual(len(row), size)
                    self.assertEqual(row.count(''), size)

    def test_check_win(self):
        # Test for a win in a row
        board_row_win = [['X', 'X', 'X'],
                         ['', '', ''],
                         ['', '', '']]
        self.assertTrue(check_win(board_row_win))

        # Test for a win in a column
        board_col_win = [['X', '', ''],
                         ['X', '', ''],
                         ['X', '', '']]
        self.assertTrue(check_win(board_col_win))

        # Test for a win in a diagonal
        board_diag_win = [['X', '', ''],
                          ['', 'X', ''],
                          ['', '', 'X']]
        self.assertTrue(check_win(board_diag_win))

        # Test for a win in the reverse diagonal
        board_reverse_diag_win = [['', '', 'O'],
                                  ['', 'O', ''],
                                  ['O', '', '']]
        self.assertTrue(check_win(board_reverse_diag_win))

        # Test for no win
        board_no_win = [['X', 'O', 'X'],
                        ['X', 'O', 'O'],
                        ['O', 'X', 'X']]
        self.assertFalse(check_win(board_no_win))

        # Test for a win with a larger board
        board_large_win = [['O', '', '', ''],
                           ['O', '', '', ''],
                           ['O', '', '', ''],
                           ['', '', '', '']]
        self.assertTrue(check_win(board_large_win))

        # Test for a win with a larger board
        board_large_win = [['O', 'O', 'O', ''],
                           ['', '', '', ''],
                           ['', '', '', ''],
                           ['', '', '', '']]
        self.assertTrue(check_win(board_large_win))

        # Test for a win with a larger board
        board_large_win = [['O', '', '', ''],
                           ['', 'O', '', ''],
                           ['', '', 'O', ''],
                           ['', '', '', '']]
        self.assertTrue(check_win(board_large_win))

        # Test for a win with a larger board
        board_large_win = [['', '', '', 'O'],
                           ['', '', 'O', ''],
                           ['', 'O', '', ''],
                           ['', '', '', '']]
        self.assertTrue(check_win(board_large_win))

        # Test for a win in a larger board (5x5)
        board_large_win_5x5 = [['X', 'X', 'X', 'X', 'X'],
                               ['', '', '', '', ''],
                               ['', '', '', '', ''],
                               ['', '', '', '', ''],
                               ['', '', '', '', '']]
        self.assertTrue(check_win(board_large_win_5x5))

if __name__ == '__main__':
    unittest.main()
