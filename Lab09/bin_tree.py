class Node:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.left = None
        self.right = None

    def __str__(self):
        return self.username


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

    def remove(self, username):  # remove and replace with inorder predecessor
        def find_max(initial):  # for inorder predecessor
            curr = initial
            while curr.right is not None:
                curr = curr.right
            return curr

        def swap_node(node_a, node_b):
            temp_user, temp_pass = node_a.username, node_a.password
            node_a.username, node_a.password = node_b.username, node_b.password
            node_b.username, node_b.password = temp_user, temp_pass

        def delete_helper(value, root):
            if root is None:  # empty tree
                return
            elif value < root.username:  # move to left node
                root.left = delete_helper(value, root.left)
            elif value > root.username:  # move to right node
                root.right = delete_helper(value, root.right)
            else:  # found deletion node
                if root.left is None and root.right is None:  # leaf
                    root = None
                elif root.left is None or root.right is None:  # node has 1 child
                    root = root.right if root.left is None else root.left
                else:  # node has 2 children
                    # find maximum predecessor
                    predecessor = find_max(root.left)
                    swap_node(predecessor, root)  # swap value
                    # delete to the left (old predecessor)
                    root.left = delete_helper(predecessor.username, root.left)
            return root
        self.root = delete_helper(username, self.root)
        return self.root

    def is_empty(self):
        return self.root is None

    def preorder(self):
        def _preorder(node):
            if node is not None:
                _preorder(node.left)
                print(node)
                _preorder(node.right)
        _preorder(self.root)

    def inorder(self):
        def _inorder(node):
            if node is not None:
                print(node)
                _inorder(node.left)
                _inorder(node.right)
        _inorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node is not None:
                _postorder(node.left)
                _postorder(node.right)
                print(node)
        _postorder(self.root)

    def print(self):
        def print_subtree(tree, level=0):
            if tree is not None:
                print_subtree(tree.right, level+1)
                print("   "*level, end="")
                print(tree.username)
                print_subtree(tree.left, level+1)
        print_subtree(self.root)


def main():
    tree = BST()
    tree.insert(Node("Best", "TestPassword"))
    tree.insert(Node("User", "Pass"))
    tree.insert(Node("Admin", "Admin"))
    tree.insert(Node("Guest", "Guest"))
    tree.insert(Node("Test", "Test"))
    tree.insert(Node("X", "P"))
    tree.insert(Node("OMG", "BST"))
    tree.print()
    print('-'*30)

    # tree.preorder()
    # tree.inorder()
    # tree.postorder()

    tree.remove('User')
    tree.print()
    print('-' * 30)


if __name__ == '__main__':
    main()
