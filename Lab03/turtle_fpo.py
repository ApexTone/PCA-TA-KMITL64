import random
import turtle


class TurtleFPO:
    def __init__(self, energy=100):
        self.t = turtle.Turtle()
        self.energy = energy

    def forward(self, value):
        if value < 0:
            raise ValueError('Error: Value must be positive')

        if self.energy - value >= 0:
            self.t.forward(value)
        else:
            self.t.forward(self.energy)
        self.energy = max(self.energy - value, 0)

    def backward(self, value):
        if value < 0:
            raise ValueError('Error: Value must be positive')

        if self.energy - value >= 0:
            self.t.backward(value)
        else:
            self.t.backward(self.energy)
        self.energy = max(self.energy - value, 0)

    def leap_forward(self, value):
        self.t.penup()
        self.forward(value)
        self.t.pendown()

    def leap_backward(self, value):
        self.t.penup()
        self.backward(value)
        self.t.pendown()


def race():
    # init turtle
    red = turtle.Turtle()
    blue = turtle.Turtle()
    green = TurtleFPO(random.randint(500, 800))
    purple = TurtleFPO(random.randint(450, 700))
    start = -400

    red.color('red')
    red.shape('turtle')
    red.up()
    red.goto(start, 50)
    red.down()

    blue.color('blue')
    blue.shape('turtle')
    blue.up()
    blue.goto(start, 25)
    blue.down()

    green.t.color('green')
    green.t.shape('turtle')
    green.t.up()
    green.t.goto(start, 0)
    green.t.down()

    purple.t.color('purple')
    purple.t.shape('turtle')
    purple.t.up()
    purple.t.goto(start, -25)
    purple.t.down()

    # finish line
    _win_x = 200
    finish = turtle.Turtle()
    finish.up()
    finish.goto(_win_x, -75)
    finish.down()
    finish.left(90)
    finish.forward(170)
    finish.hideturtle()

    # farthest = win
    while True:
        red.forward(random.randint(5, 20))
        blue.forward(random.randint(5, 20))
        green.forward(random.randint(5, 20))
        purple.forward(random.randint(5, 20))
        if red.pos()[0] >= _win_x or blue.pos()[0] >= _win_x or \
                green.t.pos()[0] >= _win_x or purple.t.pos()[0] >= _win_x:
            break

    turtle.done()


def main():
    race()


if __name__ == '__main__':
    main()
