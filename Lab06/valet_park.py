class Stack:
    def __init__(self):
        self.stack = []  # use _ for 'private'-ish variable

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception('Stack is empty')

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)
        else:
            raise Exception('Stack is empty')

    def contain(self, value):
        return value in self.stack  # you can use list.count(value) > 0 as well

    def __str__(self):
        return str(self.stack)


class ValetPark:
    def __init__(self):
        self.main_lane = Stack()
        self.temp_lane = Stack()

    def park(self, car):
        if self.main_lane.contain(car):
            print(f"Car #{car} already parked here")
            return
        self.main_lane.push(car)

    def get_car(self, car):
        if not self.main_lane.contain(car):
            print(f"Car #{car} wasn't park here")
            return
        while self.main_lane.peek() != car:
            self.temp_lane.push(self.main_lane.pop())
        print(f'Car #{self.main_lane.pop()} exiting')
        while not self.temp_lane.is_empty():
            self.main_lane.push(self.temp_lane.pop())

    def __str__(self):
        return str(self.main_lane)


def main():
    n = 5
    parking = ValetPark()

    for i in range(n):
        car_id = input(f"Input #{i+1} car's ID: ")
        parking.park(car_id)

    for i in range(n):
        car_id = input("Exiting car's ID: ")
        parking.get_car(car_id)

    print(parking)


if __name__ == '__main__':
    main()
