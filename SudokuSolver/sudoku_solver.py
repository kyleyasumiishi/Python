"""
SudokuSolver class for Sudoku solver Python program.

By: Kyle Yasumiishi
Last updated: 2/24/2018
"""

import unittest
import math

# Constants whose values are lists representing unsolved Sudoku puzzle boards

ALL_VALS = [1,2,3,4,5,6,7,8,9]

EX_PUZZLE0 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

EX_PUZZLE1 = [[8,4,0,0,0,6,7,0,0],[0,0,0,0,0,0,0,4,5],[0,0,0,0,0,8,0,0,0],
              [1,0,0,0,9,0,4,5,7],[0,0,2,0,0,0,1,0,0],[5,7,4,0,1,0,0,0,8],
              [0,0,0,3,0,0,0,0,0],[7,3,0,0,0,0,0,0,0],[0,0,9,4,0,0,5,3,2]]

EX_PUZZLE1_MOD = [[0,4,1,5,3,6,0,2,9],[3,9,6,2,0,1,8,4,0],[2,0,7,9,4,0,3,1,6],
                  [1,6,3,8,0,2,4,5,0],[0,8,2,7,5,4,1,0,3],[5,7,0,6,1,0,2,9,8],
                  [4,2,8,3,0,5,0,7,1],[7,3,0,1,0,9,6,8,4],[6,1,0,0,8,7,5,3,2]]

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

EX_PUZZLE5 = [[4,3,0,8,2,0],[],[],[],[],[],[],[],[]]

class SudokuSolver:
    """
    Class to keep track of the state of the Sudoku puzzle.
    """

    def __init__(self, height, width, puzzle_board):
        self._puzzle_height = height
        self._puzzle_width = width
        self._puzzle_board = puzzle_board

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in range(self._puzzle_height):
            print self._puzzle_board[row]

        # return str(self._puzzle_board)
        return ""

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

    def get_cell_family(self, row, col):
        """
        Return list of every non-zero cell in a given cell's row, col, and 3x3 square groups.
        """
        cell_family = []

        for cell in self.get_row_group(row):
            if self.get_cell_num(cell[0], cell[1]) != 0:
                val = self.get_cell_num(cell[0], cell[1])
                cell_family.append(val)
        for cell in self.get_col_group(col):
            if self.get_cell_num(cell[0], cell[1]) != 0:
                val = self.get_cell_num(cell[0], cell[1])
                cell_family.append(val)
        for cell in self.get_3x3_group(row, col):
            if self.get_cell_num(cell[0], cell[1]) != 0:
                val = self.get_cell_num(cell[0], cell[1])
                cell_family.append(val)

        return cell_family

    def is_valid_cell(self, row, col):
        """
        This invariant Boolean evaluates the validity of a cell.
        Returns True if the cell's value is zero, or if the
        cell's value is not already in its row, column, or 3x3 square.
        Otherwise, returns False.
        """
        cell_val = self.get_cell_num(row, col)
        cell_family = self.get_cell_family(row, col)

        # Returns True if there are three occurrences of cell_val
        # (one for row, col, and 3x3 square) in cell_family. 
        if cell_family.count(cell_val) == 3 or cell_val == 0:
            return True
        else:
            return False

    def get_possible_vals(self, row, col):
        """
        Return a list of valid possible values for a given empty cell.
        """
        cell_family = self.get_cell_family(row, col)
        possible_vals = list(set([val for val in ALL_VALS if val not in cell_family]))
        valid_vals = []
        for val in possible_vals:
            clone = self.clone()
            clone.set_cell(row, col, val)
            if clone.is_valid_cell(row, col):
                valid_vals.append(val)

        return sorted(valid_vals)

    def clone(self):
        """
        Return a copy of the Sudoku puzzle.
        """
        return SudokuSolver(self.get_height(), self.get_width(), self._puzzle_board)


# def solve_puzzle_old(obj):

#     empty_cells = obj.get_empty_cells()
#     all_vals = [1,2,3,4,5,6,7,8,9]

#     # Base case
#     if len(empty_cells) == 0:
#         return True
#     # Recursive case
#     while len(empty_cells) > 0:
#         current_empty_cell = empty_cells[0]
#         current_cell_family = obj.get_cell_family(current_empty_cell[0], current_empty_cell[1])
#         possible_vals = [val for val in all_vals if val not in current_cell_family]
        
#         # print "current_empty_cell:", current_empty_cell
#         # print "possible_vals:", possible_vals
        
#         # If no possible_vals, backtrack
#         if len(possible_vals) > 0:
            
#             clone = obj.clone()

#             # If no val in possible_vals lead to correct board, backtrack
            
#             while obj.get_cell_num(current_empty_cell[0], current_empty_cell[1]) == 0:
#                 for val in possible_vals:
#                     clone.set_cell(current_empty_cell[0], current_empty_cell[1], val)
                    
#                     # print "clone:"
#                     # print clone
#                     # print "val:", val
#                     # print "is_valid_cell:", clone.is_valid_cell(current_empty_cell[0], current_empty_cell[1])
#                     # print
#                     # print "#########################"
#                     # print

#                     # If val makes board invalid, go to next val.
#                     if clone.is_valid_cell(current_empty_cell[0], current_empty_cell[1]):
#                         if solve_puzzle(clone):
#                             obj.set_cell(current_empty_cell[0],current_empty_cell[1], val)
#                             empty_cells = obj.get_empty_cells()
#                         else:
#                             clone.set_cell(current_empty_cell[0], current_empty_cell[1], 0)
#                     else:
#                         clone.set_cell(current_empty_cell[0], current_empty_cell[1], 0)    # go to next val
                
#                 if clone.get_cell_num(current_empty_cell[0], current_empty_cell[1]) == 0:
#                     return ("No possible values result in solved board", clone._puzzle_board)    # backtrack
#         else:
#             return "No possible values exist"    # backtrack
#         empty_cells = obj.get_empty_cells()    
#     return obj._puzzle_board

EMPTY_CELL_NUM = -1

def solve_puzzle(obj):
    """

    """
    global EMPTY_CELL_NUM
    empty_cells = obj.get_empty_cells()
    EMPTY_CELL_NUM += 1

    # Base case
    if len(empty_cells) == 0:
        return True
    # Recursive case

    # While there are empty cells (i.e., len(empty_cells) > 0):
    # 1) Find all valid possible values for the first element in empty_cells (i.e., empty_cells[0])
    # 2) If there are none, return False;
    # 3) Otherwise, iterate through these valid possible values. Specifically, for each val,
    # set the cell to val and recursively call solve_puzzle. 
    # 4) If solve_puzzle returns False, reset the cell to 0.
    # 5) Otherwise, update empty_cells to empty_cells[1:] and break out of the loop. This shoudl
    # cause the while loop to go again if there are additional empty_cells.
    # 6) After the while loop, return the puzzle board.

    while len(empty_cells) > 0:
        cell = empty_cells[0]
        
        # Find all valid possible values for the first element in empty_cells (i.e., empty_cells[0])
        possible_vals = obj.get_possible_vals(cell[0], cell[1])

        # If there are no valid possible moves, return False.
        if len(possible_vals) == 0:
            return (False, EMPTY_CELL_NUM, "no valid possible moves", cell)

        # Otherwise, iterate through these possible values. Specifically, for each val,
        # set the cell to val and recursively call solve_puzzle.
        else:
            for val in possible_vals:
                obj.set_cell(cell[0], cell[1], val)
                
                # If solve_puzzle returns True, update empty_cells to empty_cells[1:] and break out of the loop.
                # This should cause us to go back to the beginning of the while loop if there are additional empty_cells.
                if solve_puzzle(obj):
                    empty_cells = empty_cells[1:]
                    break

                # Otherwise, reset the cell to 0 (i.e., empty), and go to the next val in possible_vals.
                else:
                    obj.set_cell(cell[0], cell[1], 0)
            
            # After iterating through all of the possible_vals, if none of them produce a correct puzzle, return False.
            if obj.get_cell_num(cell[0], cell[1]) == 0:
                return (False, EMPTY_CELL_NUM, "none of possible_vals produced correct puzzle", cell)

    return obj._puzzle_board













############################################################################################

EX_0 = SudokuSolver(9, 9, EX_PUZZLE0)
EX_1 = SudokuSolver(9, 9, EX_PUZZLE1)
EX_1_MOD = SudokuSolver(9, 9, EX_PUZZLE1_MOD)
EX_2 = SudokuSolver(9, 9, EX_PUZZLE2)
EX_3 = SudokuSolver(9, 9, EX_PUZZLE3)
EX_4 = SudokuSolver(9, 9, EX_PUZZLE3)

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
        self.assertEqual(solve_puzzle(EX_1_MOD), EX_PUZZLE1_SOL)
        self.assertEqual(solve_puzzle(EX_1), EX_PUZZLE1_SOL)


############################################################################################

# suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
# unittest.TextTestRunner(verbosity=2).run(suite)

# print EX_1.get_empty_cells()

print solve_puzzle(EX_1)
# for row in range(len(ans)):
#     print ans[row]
# print
# for row in range(len(EX_PUZZLE1_SOL)):
#     print EX_PUZZLE1_SOL[row]