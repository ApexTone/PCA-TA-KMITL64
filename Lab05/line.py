import random
import turtle

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    # IMO: get_x() and get_y() are redundant, I'll skip it
    def __repr__(self):
        return f"({self.x},{self.y})"  # f-string

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def distance(self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.y
        return (diff_x ** 2 + diff_y ** 2) ** 0.5


class Line:
    def __init__(self, points=None):
        if points is None:
            self.points = []
        else:
            self.points = points

    def __str__(self):
        return str(self.points)

    def join(self, line):
        self.points.extend(line.points)
        line.points.clear()

    def zigzag1(self, line):  # alter line1 and line2 into line3 (1 2 1 2 1 2)
        result = []
        while len(self.points) > 0 and len(line.points) > 0:
            if len(self.points) > 0:
                result.append(self.points.pop(0))
            if len(line.points) > 0:
                result.append(line.points.pop(0))

        while len(self.points) > 0:
            result.append(self.points.pop(0))
        while len(line.points) > 0:
            result.append(line.points.pop(0))
        return Line(result)

    def zigzag2(self, line):  # shuffle line2 into line1 (1 2 1 2 1 2, no new list)
        index = 1
        while len(line.points) > 0:
            self.points.insert(index, line.points.pop())
            index += 2

    @staticmethod
    def draw_line(line, color="black"):
        if len(line.points) <= 0:
            return
        t = turtle.Turtle()
        t.speed(5)
        t.shapesize(0.5, 0.5, 0.5)
        t.shape('circle')
        t.color(color)
        t.up()
        t.goto(line.points[0].x, line.points[0].y)
        t.stamp()
        t.down()
        for point in line.points[1:]:
            t.goto(point.x, point.y)
            t.stamp()
        t.hideturtle()


def main():
    points1 = []
    for _ in range(random.randint(3, 10)):
        points1.append(Point(random.randint(0, 300), random.randint(0, 300)))
    line1 = Line(points1)

    points2 = []
    for _ in range(random.randint(3, 10)):
        points2.append(Point(random.randint(-150, 150), random.randint(-150, 150)))
    line2 = Line(points2)

    Line.draw_line(line1, 'green')
    Line.draw_line(line2, 'red')
    print(line1)
    print(line2)
    line1.zigzag2(line2)
    Line.draw_line(line1, 'orange')
    print(line1)
    print(line2)
    turtle.done()


if __name__ == '__main__':
    main()
