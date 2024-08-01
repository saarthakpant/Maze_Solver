
from cell import Cell
import time,random

class Maze:
    def __init__(self,
                x1,
                y1,
                num_rows,
                num_cols,
                cell_size_x,
                cell_size_y,
                win=None,
                seed = None,
                ) -> None:
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    
    def _draw_cell(self,i,j):
        if self._win is None:
            return
        x1 = self._x1 + (i*self._cell_size_x)
        y1 = self._y1 + (j*self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
    
    def _create_cells(self):
        for col in range(0,self._num_cols):
            column = []
            for row in range(0,self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
            
        for x in range(0,self._num_cols):
            for y in range(0,self._num_rows):
                self._draw_cell(x,y)
                
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)
        
    def _break_walls_r(self,x,y):
        self._cells[x][y].visited = True
        while True:
            next_index_list = []
            
            # Left
            if x>0 and not self._cells[x-1][y].visited:
                next_index_list.append((x-1,y))
             
            # right   
            if x <self._num_cols -1 and not self._cells[x+1][y].visited:   
                next_index_list.append((x+1,y))
            
            # Up
            if y > 0 and not self._cells[x][y-1].visited:
                next_index_list.append((x,y-1))
            
            # Bottom
            if y<self._num_rows -1 and not self._cells[x][y+1].visited:
                next_index_list.append((x,y+1))
                
            if len(next_index_list)==0:
                self._draw_cell(x,y)
                return
            
            random_dir = random.randrange(len(next_index_list))
            next_cell = next_index_list[random_dir]
            
            if next_cell[0] == x+1:
                self._cells[x][y].has_right_wall = False
                self._cells[x+1][y].has_left_wall= False
            
            if next_cell[0] == x-1:
                self._cells[x][y].has_left_wall= False
                self._cells[x-1][y].has_right_wall = False
                
            if next_cell[1] == y+1:
                self._cells[x][y].has_bottom_wall = False
                self._cells[x][y+1].has_top_wall = False
            
            if next_cell[1] == y-1:
                self._cells[x][y].has_top_wall = False
                self._cells[x][y-1].has_bottom_wall = False
                
            self._break_walls_r(next_cell[0],next_cell[1])
            
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False