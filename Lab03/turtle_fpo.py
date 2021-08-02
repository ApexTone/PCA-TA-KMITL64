import turtle


class TurtleFPO:
    def __init__(self, energy=100):
        self.turtle = turtle.Turtle()
        self.energy = energy

    def forward(self, value):
        if value < 0:
            raise ValueError('Error: Value must be positive')

        if self.energy - value >= 0:
            self.turtle.forward(value)
        else:
            self.turtle.forward(self.energy)
        self.energy = max(self.energy - value, 0)

    def backward(self, value):
        if value < 0:
            raise ValueError('Error: Value must be positive')

        if self.energy - value >= 0:
            self.turtle.backward(value)
        else:
            self.turtle.backward(self.energy)
        self.energy = max(self.energy - value, 0)

