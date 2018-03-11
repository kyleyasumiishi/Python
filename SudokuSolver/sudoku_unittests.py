"""
Tests for sudoku_solver

By: Kyle Yasumiishi
Last updated: 3/10/2018
"""

import sudoku_solver as solver
import unittest

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

EX_PUZZLE2 = [[0,0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

EX_PUZZLE3 = [[0,0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

EX_PUZZLE4 = [[0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

EX_PUZZLE5 = [[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0],
              [8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],
              [0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]]

EX_PUZZLE5_SOL = [[4,3,5,2,6,9,7,8,1],[6,8,2,5,7,1,4,9,3],[1,9,7,8,3,4,5,6,2],
                  [8,2,6,1,9,5,3,4,7],[3,7,4,6,8,2,9,1,5],[9,5,1,7,4,3,6,2,8],
                  [5,1,9,3,2,6,8,7,4],[2,4,8,9,5,7,1,3,6],[7,6,3,4,1,8,2,5,9]]

EX_PUZZLE6 = [[0,2,0,0,0,0,0,0,0],[0,0,0,6,0,0,0,0,3],[0,7,4,0,8,0,0,0,0],
              [0,0,0,0,0,3,0,0,2],[0,8,0,0,4,0,0,1,0],[6,0,0,5,0,0,0,0,0],
              [0,0,0,0,1,0,7,8,0],[5,0,0,0,0,9,0,0,0],[0,0,0,0,0,0,0,4,0]]

EX_PUZZLE6_SOL = [[1,2,6,4,3,7,9,5,8],[8,9,5,6,2,1,4,7,3],[3,7,4,9,8,5,1,2,6],
                  [4,5,7,1,9,3,8,6,2],[9,8,3,2,4,6,5,1,7],[6,1,2,5,7,8,3,9,4],
                  [2,6,9,3,1,4,7,8,5],[5,4,8,7,6,9,2,3,1],[7,3,1,8,5,2,6,4,9]]

EX_PUZZLE7 = [[0,9,0,1,0,0,0,7,0],[0,4,0,0,0,0,0,0,6],[0,0,3,2,0,5,0,9,0],
              [0,0,0,0,0,0,7,0,0],[0,0,6,0,0,0,0,3,1],[1,0,0,6,0,8,0,0,0],
              [4,8,9,7,0,0,0,0,0],[0,2,0,0,9,0,0,0,0],[0,0,0,8,4,0,0,0,5]]

EX_PUZZLE7_SOL = [[5,9,8,1,6,4,3,7,2],[2,4,1,9,3,7,5,8,6],[7,6,3,2,8,5,1,9,4],
                  [9,5,2,4,1,3,7,6,8],[8,7,6,5,2,9,4,3,1],[1,3,4,6,7,8,2,5,9],
                  [4,8,9,7,5,2,6,1,3],[6,2,5,3,9,1,8,4,7],[3,1,7,8,4,6,9,2,5]]


############################################################################################

# SudokuSolver class instances used for testing

EX_0 = solver.SudokuSolver(9, 9, EX_PUZZLE0)
EX_1 = solver.SudokuSolver(9, 9, EX_PUZZLE1)
EX_2 = solver.SudokuSolver(9, 9, EX_PUZZLE2)
EX_3 = solver.SudokuSolver(9, 9, EX_PUZZLE3)
EX_4 = solver.SudokuSolver(9, 9, EX_PUZZLE3)
EX_5 = solver.SudokuSolver(9, 9, EX_PUZZLE5)
EX_6 = solver.SudokuSolver(9, 9, EX_PUZZLE6)
EX_7 = solver.SudokuSolver(9, 9, EX_PUZZLE7)

############################################################################################

# Unit Tests

class TestSuite(unittest.TestCase):
    """
    Test cases
    """

    # maxDiff = None

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

    def test_get_possible_vals(self):
        self.assertEqual(EX_1.get_possible_vals(0,2), [1,3,5])
        self.assertEqual(EX_1.get_possible_vals(5,5), [2,3])
        self.assertEqual(EX_1.get_possible_vals(8,1), [1,6,8])

    def test_is_valid_cell(self):
        self.assertEqual(EX_0.is_valid_cell(0,0), True)
        self.assertEqual(EX_1.is_valid_cell(0,0), True)
        self.assertEqual(EX_1.is_valid_cell(0,2), True)
        self.assertEqual(EX_1.is_valid_cell(4,6), True)
        self.assertEqual(EX_2.is_valid_cell(0,2), False)
        self.assertEqual(EX_2.is_valid_cell(0,3), True)
        self.assertEqual(EX_3.is_valid_cell(0,2), False)
        self.assertEqual(EX_4.is_valid_cell(0,2), False)

    def test_solve_puzzle(self):
        solver.solve_puzzle(EX_1)
        self.assertEqual(EX_1._puzzle_board, EX_PUZZLE1_SOL)
        solver.solve_puzzle(EX_5)
        self.assertEqual(EX_5._puzzle_board, EX_PUZZLE5_SOL)
        solver.solve_puzzle(EX_6)
        self.assertEqual(EX_6._puzzle_board, EX_PUZZLE6_SOL)
        solver.solve_puzzle(EX_7)
        self.assertEqual(EX_7._puzzle_board, EX_PUZZLE7_SOL)


############################################################################################

suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
unittest.TextTestRunner(verbosity=2).run(suite)
