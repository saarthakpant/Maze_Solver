from graphics import Window, Line, Point
from cell import Cell
        

def main():
    win = Window(800,600)
    
    c1 = Cell(win)
    c1.has_bottom_wall = False
    c1.draw(50, 50, 100, 100)
     
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(150, 150, 100, 100)

    c3 = Cell(win)
    c3.has_right_wall = False
    c3.draw(125, 125, 200, 200)

    c4 = Cell(win)
    c4.has_bottom_wall = False
    c4.draw(225, 225, 250, 250)

    c5 = Cell(win)
    c5.has_top_wall = False
    c5.draw(300, 300, 500, 500)
    
    win.wait_for_close()
    
main()