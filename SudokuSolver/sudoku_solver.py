"""
Sudoku solver
"""

import unittest
import math

# Constants whose values are lists representing unsolved Sudoku puzzle boards

EX_PUZZLE0 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

EX_PUZZLE1 = [[8,4,0,0,0,6,7,0,0],[0,0,0,0,0,0,0,4,5],[0,0,0,0,0,8,0,0,0],
              [1,0,0,0,9,0,4,5,7],[0,0,2,0,0,0,1,0,0],[5,7,4,0,1,0,0,0,8],
              [0,0,0,3,0,0,0,0,0],[7,3,0,0,0,0,0,0,0],[0,0,9,4,0,0,5,3,2]]

EX_PUZZLE1_SOL = [[8,4,1,5,3,6,7,2,9],[3,9,6,2,7,1,8,4,5],[2,5,7,9,4,8,3,1,6],
                  [1,6,3,8,9,2,4,5,7],[9,8,2,7,5,4,1,6,3],[5,7,4,6,1,3,2,9,8],
                  [4,2,8,3,6,5,9,7,1],[7,3,5,1,2,9,6,8,4],[6,1,9,4,8,7,5,3,2]]

class SudokuSolver:
    """
    Class to keep track of the state of the Sudoku puzzle.
    """

    def __init__(self, height, width, unsolved_puzzle):
        self._puzzle_height = height
        self._puzzle_width = width
        self._puzzle_board = unsolved_puzzle

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in range(self._puzzle_height):
            print self._puzzle_board[row]
        print

        return str(self._puzzle_board)

    def get_height(self):
        """
        Get the height of the puzzle board.
        """
        return self._puzzle_height

    def get_width(self):
        """
        Get the width of the puzzle board.
        """
        return self._puzzle_width

    def get_cell_num(self, row, col):
        """
        Get the value of the cell at position row, col in the puzzle board.
        """
        return self._puzzle_board[row][col]
    
    def get_empty_cells(self):
        """
        Return a list of cells in the puzzle board with a value of zero.
        """
        empty_cells = [(row, col) for row in range(self._puzzle_height) for 
                        col in range(self._puzzle_width) if self._puzzle_board[row][col] == 0]
        return empty_cells

    def set_cell(self, row, col, value):
        """
        Set the cell at position row, col to have the given value.
        """
        self._puzzle_board[row][col] = value

    def get_row_group(self, row):
        """
        Returns a list of cells in the given row of the puzzle board.
        """
        row_group = []
        for col in range(self.get_width()):
            row_group.append((row, col))
        return row_group

    def get_col_group(self, col):
        """
        Returns a list of cells in the given column of the puzzle board.
        """
        col_group = []
        for row in range(self.get_height()):
            col_group.append((row, col))
        return col_group

    def get_3x3_group(self, row, col):
        """
        Returns a list of cells in the same 3x3 square as the cell
        at position row, col.
        """
        row0 = int(math.floor((3 * row) / self.get_height()) * 3)
        row1 = row0 + 1
        row2 = row0 + 2
        col0 = int(math.floor((3 * col) / self.get_width()) * 3)
        col1 = col0 + 1
        col2 = col0 + 2

        square_group = [(row0,col0),(row0,col1),(row0,col2),
                        (row1,col0),(row1,col1),(row1,col2),
                        (row2,col0),(row2,col1),(row2,col2)]

        return square_group


############################################################################################

EX_0 = SudokuSolver(9, 9, EX_PUZZLE0)
EX_1 = SudokuSolver(9, 9, EX_PUZZLE1)

class TestSuite(unittest.TestCase):
    """
    Test cases
    """

    def test_get_3x3_group(self):
        self.assertEqual(EX_0.get_3x3_group(5,2), [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)], msg=str(EX_0.get_3x3_group(5,2)))
        self.assertEqual(EX_0.get_3x3_group(6,2), [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)], msg=str(EX_0.get_3x3_group(6,2)))
        self.assertEqual(EX_0.get_3x3_group(4,4), [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)], msg=str(EX_0.get_3x3_group(4,4)))
        self.assertEqual(EX_0.get_3x3_group(8,7), [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)], msg=str(EX_0.get_3x3_group(8,7)))
        self.assertEqual(EX_0.get_3x3_group(0,8), [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)], msg=str(EX_0.get_3x3_group(0,8)))

    def test_get_col_group(self):
        self.assertEqual(EX_0.get_col_group(0), [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)], msg=str(EX_0.get_col_group(0)))
        self.assertEqual(EX_0.get_col_group(1), [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)], msg=str(EX_0.get_col_group(1)))
        self.assertEqual(EX_0.get_col_group(3), [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)], msg=str(EX_0.get_col_group(3)))
        self.assertEqual(EX_0.get_col_group(6), [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)], msg=str(EX_0.get_col_group(6)))
        self.assertEqual(EX_0.get_col_group(8), [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)], msg=str(EX_0.get_col_group(8)))

    def test_get_row_group(self):
        self.assertEqual(EX_0.get_row_group(0), [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)], msg=str(EX_0.get_row_group(0)))
        self.assertEqual(EX_0.get_row_group(2), [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], msg=str(EX_0.get_row_group(2)))
        self.assertEqual(EX_0.get_row_group(3), [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)], msg=str(EX_0.get_row_group(3)))
        self.assertEqual(EX_0.get_row_group(4), [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)], msg=str(EX_0.get_row_group(4)))
        self.assertEqual(EX_0.get_row_group(8), [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)], msg=str(EX_0.get_row_group(8)))

    def test_get_cell_num(self):
        self.assertEqual(EX_1.get_cell_num(2, 0), 0, msg="(2,0)")
        self.assertEqual(EX_1.get_cell_num(2, 5), 8, msg="(2,5)")
        self.assertEqual(EX_1.get_cell_num(4, 2), 2, msg="(4,2)")
        self.assertEqual(EX_1.get_cell_num(4, 6), 1, msg="(4,6)")
        self.assertEqual(EX_1.get_cell_num(7, 8), 0, msg="(7,8)")
        self.assertEqual(EX_1.get_cell_num(8, 8), 2, msg="(8,8)")

    def test_get_empty_cells(self):
        self.assertEqual(EX_1.get_empty_cells(), [(0, 2), (0, 3), (0, 4), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), 
                                                  (1, 5), (1, 6), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 8), 
                                                  (3, 1), (3, 2), (3, 3), (3, 5), (4, 0), (4, 1), (4, 3), (4, 4), (4, 5), (4, 7), 
                                                  (4, 8), (5, 3), (5, 5), (5, 6), (5, 7), (6, 0), (6, 1), (6, 2), (6, 4), (6, 5), 
                                                  (6, 6), (6, 7), (6, 8), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), 
                                                  (8, 0), (8, 1), (8, 4), (8, 5)])

    def test_3x3_group_values(self):
        test_square_group = EX_1.get_3x3_group(4,2)
        test_square_group_values = []
        for cell in test_square_group:
            test_square_group_values.append(EX_1.get_cell_num(cell[0], cell[1]))
        self.assertEqual(test_square_group_values, [1, 0, 0, 0, 0, 2, 5, 7, 4], msg=str(test_square_group_values))

############################################################################################

suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
unittest.TextTestRunner(verbosity=2).run(suite)

