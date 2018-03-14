"""
Sudoku GUI

By: Kyle Yasumiishi
Adapted From: newcoder.io Sudoku Tutorial Part 3: Implementing the GUI
http://newcoder.io/gui/part-3/
Last Updated: 3/13/2018
"""

from Tkinter import *
import sudoku_solver as solver

################################################################

# Constants

GUI_MARGIN = 20
CELL_SIZE = 40
GUI_WIDTH = (CELL_SIZE * 9) + (GUI_MARGIN * 2)
GUI_HEIGHT = GUI_WIDTH

################################################################

# SudokuGUI Class

class SudokuGUI(Frame):

    def __init__(self, parent, solver_obj):
        self._parent = parent
        self._solver = solver_obj
        Frame.__init__(self, parent)
        self.__initUI()

    def __initUI(self):
        """
        Sets up user interface of Sudoku puzzle.
        """
        # Title
        self._parent.title("Sudoku Solver")
        # Canvas
        self._canvas = Canvas(self._parent, width=GUI_WIDTH, height=GUI_HEIGHT)
        self._canvas.pack(fill=BOTH, side=TOP)
        # Solve Button
        self._solve_button = Button(self._parent, text="Solve")
        self._solve_button.pack(fill=BOTH, side=BOTTOM)
        # Check Answers Button
        self._check_answers_button = Button(self._parent, text="Check Answers")
        self._check_answers_button.pack(fill=BOTH, side=BOTTOM)
        # Reset Button
        self._reset_button = Button(self._parent, text="Reset")
        self._reset_button.pack(fill=BOTH, side=BOTTOM)
        # Draw Grid
        self.__draw_grid()
        # Draw puzzle
        self.__draw_puzzle()
        # Bind Keys
        # self._canvas.bind("<Button-1>", )
        # self._canvas.bind("<Key>", )

    def __draw_grid(self):
        """
        Draws grid
        """
        for idx in range(10):
            line_width = 4 if idx % 3 == 0 else 1
            # Vertical lines
            x0 = GUI_MARGIN + idx * CELL_SIZE
            y0 = GUI_MARGIN
            x1 = GUI_MARGIN + idx * CELL_SIZE
            y1 = GUI_HEIGHT - GUI_MARGIN
            self._canvas.create_line(x0, y0, x1, y1, fill="black", width=line_width)
            # Horizontal lines
            x0 = GUI_MARGIN
            y0 = GUI_MARGIN + idx * CELL_SIZE
            x1 = GUI_WIDTH - GUI_MARGIN
            y1 = GUI_MARGIN + idx * CELL_SIZE
            self._canvas.create_line(x0, y0, x1, y1, fill="black", width=line_width)

    def __draw_puzzle(self):
        """
        Draws puzzle numbers
        """
        for row in range(self._solver.get_height()):
            for col in range(self._solver.get_width()):
                cell_num = self._solver.get_cell_num(row, col)
                if cell_num != 0:
                    x = GUI_MARGIN + col * CELL_SIZE + CELL_SIZE / 2
                    y = GUI_MARGIN+  row * CELL_SIZE + CELL_SIZE / 2
                    original = self._solver._initial_board[row][col]
                    text_color = "black" if cell_num == original else "blue"
                    self._canvas.create_text(x, y, text=cell_num, fill=text_color)

    def run(self):
        self.mainloop()

################################################################

root = Tk()
gui = SudokuGUI(root, solver.SudokuSolver(puzzle_board=[[8,4,0,0,0,6,7,0,0],[0,0,0,0,0,0,0,4,5],[0,0,0,0,0,8,0,0,0],[1,0,0,0,9,0,4,5,7],[0,0,2,0,0,0,1,0,0],[5,7,4,0,1,0,0,0,8],[0,0,0,3,0,0,0,0,0],[7,3,0,0,0,0,0,0,0],[0,0,9,4,0,0,5,3,2]]))
gui.run()