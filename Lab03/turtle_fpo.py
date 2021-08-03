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


def test_fpo():
    fpot = TurtleFPO(500)
    while fpot.energy > 0:
        fpot.leap_forward(random.randint(10, 50))
        print('leap')


def race():
    red = turtle.Turtle()
    blue = turtle.Turtle()
    green = TurtleFPO(700)
    purple = TurtleFPO(700)
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

    # farthest = win
    for _ in range(50):
        red.forward(random.randint(5, 20))
        blue.forward(random.randint(5, 20))
        green.t.forward(random.randint(5, 20))
        purple.t.forward(random.randint(5, 20))

    turtle.done()


def main():
    race()


if __name__ == '__main__':
    main()
