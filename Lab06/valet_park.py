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


def main():
    n = 5
    parking = Stack()
    buffer = Stack()

    for i in range(n):
        car_id = input(f"Input #{i+1} car's ID: ")
        if not parking.contain(car_id):
            parking.push(car_id)
        else:
            print(f"Car with ID: {car_id} already parked here")

    for i in range(n):
        car_id = input("Exiting car's ID: ")
        if not parking.contain(car_id):
            print(f"Car with ID: {car_id} wasn't park here")
        else:
            while parking.peek() != car_id:
                buffer.push(parking.pop())
            # This is only to show the concept. Normally, stack field would be private so it can't be access here
            print(f"Buffer: {buffer.stack}")
            print(f"Exiting: {parking.pop()}")
            print(f"Parking: {parking.stack}")
            while not buffer.is_empty():
                parking.push(buffer.pop())


if __name__ == '__main__':
    main()
