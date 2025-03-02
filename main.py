from window import Window
from line import Line
from point import Point
from cell import Cell


def main():
    win = Window(800, 600)
    point_1 = Point(25, 25)
    point_2 = Point(50, 50)
    point_3 = Point(50, 25)
    point_4 = Point(75, 50)
    cell_1 = Cell(win)
    cell_1.draw(point_1, point_2)
    cell_2 = Cell(win)
    cell_2.draw(point_3, point_4)
    cell_1.draw_move(cell_2)
    win.wait_for_close()

main()