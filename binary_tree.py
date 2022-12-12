# binary tree via linked list


from queue import Queue


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"


class BinaryTree():
    def __init__(self, node):
        self.head = node

    def pre_order_traversal(self, node="first"):
        if node == "first":
            node = self.head

        if node:
            print(node)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node="first"):
        if node == "first":
            node = self.head

        if node:
            self.in_order_traversal(node.left)
            print(node)
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node="first"):
        if node == "first":
            node = self.head
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node)

    def level_order_traversal(self):
        a_queue = Queue()
        a_queue.put(self.head)
        while not a_queue.empty():
            node = a_queue.get()
            if node.left:
                a_queue.put(node.left)
            if node.right:
                a_queue.put(node.right)
            print(node.value)

    # def search(self, value, node="first",):
    #     if node == "first":
    #         node = self.head
    #     else:
    #         pass
    #     if node:
    #         if node.value == value:
    #             return node
    #     if node:
    #         temp_node = self.search(value, node.left)
    #         if temp_node:
    #             if temp_node.value == value:
    #                 return temp_node
    #         temp_node = self.search(value, node.right)
    #         if temp_node:
    #             if temp_node.value == value:
    #                 return temp_node
    #     return node

    def search(self, value):
        a_queue = Queue()
        a_queue.put(self.head)
        while not a_queue.empty():
            node = a_queue.get()
            if node.value == value:
                return node
            if node.left:
                a_queue.put(node.left)
            if node.right:
                a_queue.put(node.right)
        print("value not found")
        return None

    def add_node(self, location, value):
        node_loc = self.search(location)
        if node_loc.left == None:
            node_loc.left = Node(value)
        elif node_loc.right == None:
            node_loc.right = Node(value)
        else:
            print("Please Select a node with a free space")
        return

    def get_deepest_node(self):
        a_queue = Queue()
        a_queue.put(self.head)
        while not a_queue.empty():
            node = a_queue.get()
            if node.left:
                a_queue.put(node.left)
            if node.right:
                a_queue.put(node.right)
        return node

    def remove_node(self, value):
        target = self.search(value)
        if not target:
            return
        deepest_node = self.get_deepest_node()
        a_queue = Queue()
        a_queue.put(self.head)
        while not a_queue.empty():
            node = a_queue.get()
            if node.right.value == deepest_node.value:
                target.value = deepest_node.value
                node.right = None
                return
            if node.left.value == deepest_node.value:
                target.value = deepest_node.value
                node.left = None
                return
            if node.left:
                a_queue.put(node.left)
            if node.right:
                a_queue.put(node.right)
        return None


head_node = Node(1)
bin_tree = BinaryTree(head_node)
bin_tree.add_node(1, 2)
bin_tree.add_node(1, 3)
bin_tree.add_node(2, 4)
bin_tree.add_node(2, 5)
bin_tree.add_node(3, 6)
bin_tree.add_node(3, 7)
print("preorder")
bin_tree.pre_order_traversal()
print("post_order")
bin_tree.post_order_traversal()
print('in_order')
bin_tree.in_order_traversal()
print("level order")
bin_tree.level_order_traversal()
bin_tree.remove_node(3)
print("remove item")
bin_tree.level_order_traversal()
