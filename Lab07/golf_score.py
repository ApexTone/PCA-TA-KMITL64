class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Golfer {self.name} has score = {self.score}"

    def __repr__(self):
        return f"{self.name}-{self.score}"

    def __eq__(self, other):
        return self.name == other.name and self.score == other.score

    def __ge__(self, other):
        return self.score >= other.score


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next_node
        return count

    # use this method to update data
    def node_at(self, pos):
        if 0 <= pos < self.size():
            curr = self.head
            count = 0
            while curr is not None:
                if count == pos:
                    break
                count += 1
                curr = curr.next_node
            return curr
        else:
            raise RuntimeError('Index out of bound')

    def value_at(self, pos):
        temp = self.node_at(pos)
        if temp is not None:
            return temp.value
        return

    def is_empty(self):
        return self.head is None

    def _push_back(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, prev_node=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def _push_front(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head.prev_node = new_node
            self.head = new_node

    def _pop_back(self):
        if self.is_empty():
            raise RuntimeError("Can't pop_back: empty list")
        else:
            value = self.tail.value
            prev = self.tail.prev_node
            self.tail.prev_node = None
            self.tail = prev
            if prev is not None:
                prev.next_node = None
            else:
                self.head = self.tail = None
            return value

    def _pop_front(self):
        if self.is_empty():
            raise RuntimeError("Can't pop_front: empty list")
        else:
            value = self.head.value
            next_node = self.head.next_node
            self.head.next_node = None
            self.head = next_node
            if next_node is not None:
                next_node.prev_node = None
            else:
                self.head = self.tail = None
            return value

    def _insert(self, pos, value):
        if pos == 0 or self.is_empty():
            self._push_front(value)
        elif pos >= self.size():
            self._push_back(value)
        elif pos < 0:  # insert from back (index of self.tail.prev_node = -1)
            pos = self.size()+pos  # change pos to positive value
            if pos <= 0:
                self._push_front(value)
            else:
                curr = self.node_at(pos)
                prev = curr.prev_node
                new_node = Node(value, curr, prev)
                prev.next_node = new_node
                curr.prev_node = new_node
        else:
            curr = self.node_at(pos)
            prev = curr.prev_node
            new_node = Node(value, curr, prev)
            prev.next_node = new_node
            curr.prev_node = new_node

    def pop(self, pos):
        if self.is_empty():
            raise RuntimeError("Can't pop: list is empty")
        elif pos == 0:
            return self._pop_front()
        elif pos == self.size()-1:
            return self._pop_back()
        elif 0 <= pos < self.size():
            curr = self.node_at(pos)
            prev_node = curr.prev_node
            next_node = curr.next_node
            prev_node.next_node = next_node
            next_node.prev_node = prev_node
            curr.prev_node = None
            curr.next_node = None
            return curr.value

    def index_of(self, value):
        curr = self.head
        count = 0
        while curr is not None:
            if curr.value == value:
                return count
            curr = curr.next_node
            count += 1
        return -1

    def remove(self, value):
        pos = self.index_of(value)
        if pos != -1:
            if pos == 0:
                self._pop_front()
            elif pos == self.size()-1:
                self._pop_back()
            else:
                self.pop(pos)
        else:
            print("Empty list or no such value")
            return

    def __str__(self):
        lst = []
        curr = self.head
        while curr is not None:
            lst.append(curr.value)
            curr = curr.next_node
        return str(lst)

    # use this method to insert (others are helper method for this)
    def add(self, value):  # insert in ascending order
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            count = 0
            buffer = self.head
            while buffer is not None:
                if buffer.value >= value:
                    self._insert(count, value)
                    return
                count += 1
                buffer = buffer.next_node
            self._push_back(value)

    def show_list(self, order="DSC"):
        result = ""
        if order == "DSC":
            curr = self.tail
            while curr is not None:
                result += str(curr.value) + "\n"
                curr = curr.prev_node
        elif order == "ASC":
            curr = self.head
            while curr is not None:
                result += str(curr.value) + "\n"
                curr = curr.next_node
        print(result, end="")

    # This method is for using with Golfer class
    def show_same_score(self, name):
        curr = self.head
        score = -1
        while curr is not None:
            if curr.value.name == name:
                score = curr.value.score
                break
            curr = curr.next_node

        result = f"Golfer with score of {score} is(are): "
        curr = self.head
        while curr is not None:
            if curr.value.score == score:
                result += curr.value.name + " "
            curr = curr.next_node
        print(result)


def main():
    golfers = DoublyLinkedList()
    golfers.add(Golfer("Pease", 74))
    golfers.add(Golfer("Walker", 76))
    golfers.add(Golfer("Mackay", 77))
    golfers.add(Golfer("Klomps", 76))
    golfers.add(Golfer("John", 56))
    golfers.add(Golfer("Dave", 99))
    golfers.add(Golfer("Jeff", 99))
    golfers.add(Golfer("Geoff", 99))
    golfers.show_list("ASC")
    golfers.show_list("DSC")
    golfers.show_same_score("Geoff")


if __name__ == '__main__':
    main()

