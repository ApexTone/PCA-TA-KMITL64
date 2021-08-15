class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # getData()/setData() and getNext()/setNext() is redundant here, I'll skipped it


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None  # use 'is' instead of ==

    def add(self, item):
        if self.is_empty():
            self.head = Node(item)
            return
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                prev = current
                current = current.next
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def squish(self):
        current = self.head
        while current is not None:
            next_node = current.next
            if next_node is not None and current.data == next_node.data:
                current.next = next_node.next
                next_node.next = None
            else:
                current = current.next

    def dble(self):
        current = self.head
        while current is not None:
            temp = Node(current.data)
            temp.next = current.next
            current.next = temp
            current = temp.next

    def show_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


def main():
    lst = UnorderedList()
    lst.add(0)
    lst.add(0)
    lst.add(0)
    lst.add(0)
    lst.add(1)
    lst.add(0)
    lst.add(0)
    lst.add(0)
    lst.add(3)
    lst.add(3)
    lst.add(3)
    lst.add(1)
    lst.add(1)
    lst.add(0)
    lst.show_list()
    lst.dble()
    lst.show_list()
    lst.squish()
    lst.show_list()


if __name__ == '__main__':
    main()
