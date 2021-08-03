import turtle


class Clock:
    def __init__(self, radius=100):
        turtle.mode('logo')
        self.t = turtle.Turtle()
        self.t.speed(0)
        self._radius = radius
        self._short_line = self._radius/50
        self._long_line = self._radius/10

    def _clock_face(self):
        for i in range(12):
            for j in range(5):
                self.t.seth(30*i + 6*j)
                self.t.up()
                self.t.forward(self._radius)
                self.t.down()
                if j == 0:
                    self.t.pensize(3)
                    self.t.forward(self._long_line)
                    self.t.up()
                    self.t.backward(self._long_line + self._radius)
                else:
                    self.t.pensize(2)
                    self.t.forward(self._short_line)
                    self.t.up()
                    self.t.backward(self._short_line+self._radius)

    def clock_hand(self, h, m, s):
        def _arrow_head(color):
            _arrow_side = self._radius/10.0
            self.t.fillcolor(color)
            self.t.begin_fill()
            self.t.left(90)
            self.t.forward(_arrow_side/2)
            self.t.right(120)
            self.t.forward(_arrow_side)
            self.t.right(120)
            self.t.forward(_arrow_side)
            self.t.right(120)
            self.t.forward(_arrow_side/2)
            self.t.right(90)
            self.t.end_fill()

        self.t.down()
        # second hand
        # 1 sec = 360/60 = 6 degree
        self.t.color('green')
        self.t.seth(s*6)
        self.t.forward(self._radius*0.9)
        _arrow_head('green')
        self.t.backward(self._radius*0.9 + (self._radius*0.1))
        self.t.goto(0, 0)

        # minute hand
        # 60 sec => 1 min => 360/60 = 5 degree
        # 60 sec = 5 degree
        # 1 sec = 5/60 = 1/12 degree
        self.t.color('orange')
        self.t.seth(m * 6 + s/12.0)
        self.t.forward(self._radius*0.8)
        _arrow_head('orange')
        self.t.backward(self._radius*0.8 + (self._radius*0.1))
        self.t.goto(0, 0)

        # hour hand
        # 3600 sec => 60 min => 1hr = 30 degree
        # 3600 sec = 30 degree
        # 1 sec = 30/3600 = 1/120 degree
        self.t.pensize(3)
        self.t.color('red')
        self.t.seth((h % 12) * 30 + (m*60 + s)/120.0)
        self.t.forward(self._radius*0.6)
        _arrow_head('red')
        self.t.backward(self._radius*0.6 + (self._radius*0.1))
        self.t.goto(0, 0)

        self.t.hideturtle()

    def draw(self, h=12, m=0, s=0):
        if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
            self._clock_face()
            self.clock_hand(h, m, s)
        else:
            raise ValueError('Hours, Minutes, Seconds must be valid value in 24h format')


def main():
    clock = Clock(100)
    h, m, s = list(map(int, input("Please tell time in this format hh:mm:ss ").split(':')))
    clock.draw(h, m, s)
    turtle.done()


if __name__ == '__main__':
    main()
