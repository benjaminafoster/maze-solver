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

    def draw(self, tl_point, lr_point): # tl = top left; lr = lower right
        self.x1 = tl_point.x
        self.y1 = tl_point.y
        self.x2 = lr_point.x
        self.y2 = lr_point.y
        if self.has_left_wall:
            left_wall = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bottom_wall, "black")

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
