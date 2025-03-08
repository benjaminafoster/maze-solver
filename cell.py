from point import Point
from line import Line

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2): # tl = top left; lr = lower right
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(left_wall, "black")
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(left_wall, "white")
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(right_wall, "black")
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(right_wall, "white")
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(top_wall, "black")
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(top_wall, "white")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(bottom_wall, "black")
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "grey"
        else:
            line_color = "red"
        # 
        center_self = Point((self.x2 + self.x1)/2, (self.y2 + self.y1)/2)
        center_other = Point((to_cell.x2 + to_cell.x1)/2, (to_cell.y2 + to_cell.y1)/2)
        line = Line(center_self, center_other)
        self.win.draw_line(line, line_color)
