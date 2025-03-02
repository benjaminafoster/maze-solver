from window import Window
from line import Line
from point import Point


def main():
    win = Window(800, 600)
    point_1 = Point(25, 25)
    point_2 = Point(25, 300)
    line = Line(point_1, point_2)
    win.draw_line(line, "red")
    win.wait_for_close()

main()