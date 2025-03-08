from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze_1 = Maze(75, 50, 10, 10, 50, 50, win, 10)
    win.wait_for_close()

main()