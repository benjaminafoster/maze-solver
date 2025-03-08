import time
import random
from cell import Cell
from point import Point

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = [] # list of lists. each top-level list is a column of cells
        
        if seed != None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrace_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        


    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells_list = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                col_cells_list.append(cell)
            self._cells.append(col_cells_list)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
                

    def _draw_cell(self, i, j):
        #print(f"cell size x: {self.cell_size_x}")
        tl_x_pos = (i * self.cell_size_x) + self.x1
        tl_y_pos = (j * self.cell_size_y) + self.y1
        lr_x_pos = tl_x_pos + self.cell_size_x
        lr_y_pos = tl_y_pos + self.cell_size_y
        self._cells[i][j].draw(tl_x_pos, tl_y_pos, lr_x_pos, lr_y_pos)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrace_and_exit(self): 
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols -1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            
            # determine which cell(s) to visit next
            #left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))

            # right
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))

            # up
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))

            # down
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))

            # if there is nowhere to go, break out...base case
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            # randomly choose the next direction to go
            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]

            # knock out walls between this cell and the next cell
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False

            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False

            #up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False