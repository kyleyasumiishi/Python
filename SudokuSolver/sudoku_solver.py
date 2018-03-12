"""
SudokuSolver class for Sudoku solver Python program.

By: Kyle Yasumiishi
Last updated: 3/11/2018
"""

import math
from copy import deepcopy

#########################################################################

# CONSTANTS

ALL_VALS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#########################################################################

# SudokuSolver Class

class SudokuSolver():
    """
    Class to keep track of the state of the Sudoku puzzle.
    """

    def __init__(self, puzzle_board=None):
        self._puzzle_height = 9
        self._puzzle_width = 9
        if puzzle_board == None:
            self._puzzle_board = [[0 for dummy_col in range(self._puzzle_width)]
                                   for dummy_row in range(self._puzzle_height)]
        else:
            self._puzzle_board = puzzle_board

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        ans = ""
        for row in range(self._puzzle_height):
            ans += str(self._puzzle_board[row]) + "\n"
        return ans

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

    def is_empty(self, row, col):
        """
        Return True if cell is empty; False otherwise.
        """
        if self.get_cell_num(row, col) == 0:
            return True
        else:
            return False

    def set_cell(self, row, col, value):
        """
        Set the cell at position row, col to have the given value.
        """
        self._puzzle_board[row][col] = value

    def unset_cell(self, row, col):
        """
        Set the cell at position row, col to have the value zero (i.e., empty cell).
        """
        self._puzzle_board[row][col] = 0

    def clear_board(self):
        """
        Sets the value of every cell to 0 (i.e., empty).
        """
        self._puzzle_board = [[0 for dummy_col in range(self.get_width())]
                               for dummy_row in range(self.get_height())]

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
        # Rows
        row0 = int(math.floor(row / math.sqrt(self.get_height())) * math.sqrt(self.get_height()))
        row1 = row0 + 1
        row2 = row0 + 2
        # Columns
        col0 = int(math.floor(col / math.sqrt(self.get_width())) * math.sqrt(self.get_width()))
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
        cells = self.get_row_group(row) + self.get_col_group(col) + self.get_3x3_group(row, col)
        vals = [self.get_cell_num(cell[0], cell[1]) for cell in cells if self.get_cell_num(cell[0], cell[1]) != 0]
        return vals

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
        return deepcopy(self)

#########################################################################

# Functions to solve a Sudoku puzzle

def backtracker(obj):
    """
    Returns True if the given SudokuSolver object is solvable using recursive backtracking.
    Helper function for solve_puzzle.
    """
    empty_cells = obj.get_empty_cells()
    # Base
    if len(empty_cells) == 0:
        return True
    # Recursive
    else:
        current_cell = empty_cells[0]
        possible_vals = obj.get_possible_vals(current_cell[0], current_cell[1])
        if len(possible_vals) > 0:
            for val in possible_vals:
                obj.set_cell(current_cell[0], current_cell[1], val)
                if backtracker(obj):
                    return True
                else:
                    obj.set_cell(current_cell[0], current_cell[1], 0)

def solve_puzzle(obj):
    """
    Takes a SudokuSolver object and solves it. Returns None.
    """
    empty_cells = obj.get_empty_cells()
    for cell in empty_cells:
        for val in ALL_VALS:
            obj.set_cell(cell[0], cell[1], val)
            if obj.is_valid_cell(cell[0], cell[1]) and backtracker(obj):
                break 
            else:
                obj.unset_cell(cell[0], cell[1])
    return None

