"""
Sudoku solver program

By: Kyle Yasumiishi
Last updated: 2/24/2018
"""

from sudoku_solver import SudokuSolver as solver
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

def solve_puzzle(solver):
    empty_cells = solver.get_empty_cells()
    print empty_cells
    # for cell in empty_cells:
    #     possible_vals = sorted(solver.)

e1 = solver(9, 9, EX_PUZZLE1)

solve_puzzle(e1)