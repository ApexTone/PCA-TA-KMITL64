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
    result = {}

    if len(points) < 2:  # error case
        result['error'] = "Points list must contain more than 1 point"
        return result

    for index, point1 in enumerate(points):
        for point2 in points[index+1:]:
            dist = point1.distance(point2)
            if dist < result.get('min_dist', float('inf')):  # if no 'min_dist', use value of float('inf) instead
                result['min_dist'] = dist
                result['p1'] = point1
                result['p2'] = point2
    return result


def main():
    points = [Point(93, 7), Point(0, 0), Point(1, 1)]
    print(find_closest(points))


if __name__ == '__main__':
    main()
