# Before refactoring
def draw_line(xBegin: int, yBegin: int, xEnd: int, yEnd: int, red: int, green: int, blue: int, alpha: int):
    pass


# Refactored

class Point:
    def __init__(self, xBegin, yBegin: int):
        pass


class Color:
    def __init__(self, red: int, green: int, blue: int, alpha: int):
        pass


def draw_line(begin: Point, end: Point, colour: Color):
    pass


begin = Point(1, 4)
end = Point(5, 10)
color = Color(237, 12, 4, 1)
draw_line(begin, end, color)