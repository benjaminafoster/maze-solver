from window import Window
from line import Line
from point import Point
from cell import Cell


def main():
    win = Window(800, 600)
    point_1 = Point(25, 25)
    point_2 = Point(50, 50)
    point_3 = Point(75, 75)
    point_4 = Point(100, 100)
    cell_1 = Cell(win).draw(point_1, point_2)
    cell_2 = Cell(win).draw(point_3, point_4)
    win.wait_for_close()

main()