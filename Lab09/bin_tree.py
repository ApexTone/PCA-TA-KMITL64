class Node:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return
        self.__insert_node(self.root, new_node)

    def __insert_node(self, current_node, new_node):
        if new_node.username <= current_node.username:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.__insert_node(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.__insert_node(current_node.right, new_node)

    def find(self, username):
        return self.__find_node(self.root, username)

    def __find_node(self, current_node, username):
        if current_node is None:
            return

        if current_node.username == username:
            return current_node
        if current_node.username < username:
            return self.__find_node(current_node.right, username)
        else:
            return self.__find_node(current_node.left, username)

    def remove(self, username):  # remove and replace with inorder successor
        pass

    def is_empty(self):
        return self.root is None

    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass

    def print_subtree(self, tree, level=0):
        if tree is not None:
            self.print_subtree(tree.right, level+1)
            print("   "*level, end="")
            print(tree.username)
            self.print_subtree(tree.left, level+1)


def main():
    tree = BST()
    tree.insert(Node("Best", "TestPassword"))
    tree.insert(Node("User", "Pass"))
    tree.insert(Node("Admin", "Admin"))
    tree.insert(Node("Guest", "Guest"))
    tree.insert(Node("Test", "Test"))
    tree.insert(Node("X", "P"))
    tree.insert(Node("OMG", "BST"))
    tree.print_subtree(tree.root)


if __name__ == '__main__':
    main()
