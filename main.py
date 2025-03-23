from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
import sys


def main():
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)
    sys.setrecursionlimit(10000)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created!")

    is_solvable = maze._solve()
    if not is_solvable:
        print("Maze is not solvable")
    else:
        print("Maze solved!")

    win.wait_for_close()

main()
