class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # Binary Search Tree cannot have duplicates
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # Visit left tree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []

        # visit base node
        elements.append(self.data)

        # Visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        elements = self.in_order_traversal()
        return elements[0]

    def find_max(self):
        elements = self.in_order_traversal()
        return elements[-1]

    def calculate_sum(self):
        elements = self.in_order_traversal()
        return sum(elements)


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    # numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers = [15, 12, 27, 7, 14, 20, 88, 23]
    numbers_tree = build_tree(numbers)

    # print(numbers_tree.pre_order_traversal())
    # print(numbers_tree.search(21))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
