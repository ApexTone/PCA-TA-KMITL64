class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # IMO: get_x() and get_y() are redundant, I'll skip it
    def __repr__(self):
        return f"({self.x},{self.y})"  # f-string

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def distance(self, other):
        diff_x = self.x-other.x
        diff_y = self.y-other.y
        return (diff_x**2 + diff_y**2)**0.5


def find_closest(points):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
