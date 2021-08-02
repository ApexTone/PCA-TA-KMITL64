import turtle


def basic():
    my_window = turtle.Screen()
    my_window.bgcolor("blue")

    my_pen = turtle.Turtle()
    my_pen.forward(150)
    my_pen.left(90)
    my_pen.forward(75)
    my_pen.color("white")
    my_pen.pensize(12)
    turtle.done()


def square():
    my_pen = turtle.Turtle()
    for i in range(4):
        my_pen.forward(150)
        my_pen.left(90)
    turtle.done()


def star():
    my_pen = turtle.Turtle()
    for i in range(5):
        my_pen.forward(50)
        my_pen.right(144)
    turtle.done()


def polygon(num_sides=6, side_length=70):
    pen = turtle.Turtle()
    angle = 360.0/num_sides
    for i in range(num_sides):
        pen.forward(side_length)
        pen.right(angle)
    turtle.done()


def spiral_square():
    my_window = turtle.Screen()
    my_window.bgcolor("light blue")
    my_window.title("Spiral Turtle")
    pen = turtle.Turtle()
    pen.color("black")

    def drawer(size):
        for i in range(4):
            pen.forward(size)
            pen.left(90)
            size -= 5

    drawer(146)
    drawer(126)
    drawer(106)
    drawer(86)
    drawer(66)
    drawer(46)
    drawer(26)
    turtle.done()


def dizzy():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    _length = len(colors)
    pen = turtle.Pen()
    turtle.bgcolor("black")
    for i in range(360):
        pen.pencolor(colors[i % _length])
        pen.width(i//100 + 1)
        pen.forward(i)
        pen.left(59)
    turtle.done()


def main():
    dizzy()


if __name__ == '__main__':
    main()
