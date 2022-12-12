from queue import Queue


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return f"{self.value}"


class AVLTree():
    def __init__(self, node):
        self.head = Node(node)

    def in_order_traversal(self, node="first"):
        if node == "first":
            node = self.head
        if node:
            self.in_order_traversal(node.left)
            print(node)
            self.in_order_traversal(node.right)

    def level_order_traversal(self):
        aqueue = Queue()
        aqueue.put(self.head)
        while not aqueue.empty():
            node = aqueue.get()
            if node.left:
                aqueue.put(node.left)
            if node.right:
                aqueue.put(node.right)
            print(node)

    def level_order_traversal_height(self):
        aqueue = Queue()
        aqueue.put(self.head)
        while not aqueue.empty():
            node = aqueue.get()
            if node.left:
                aqueue.put(node.left)
            if node.right:
                aqueue.put(node.right)
            print(node.height)

    def get_height(self, node):
        if node:
            return node.height
        return 0

    def get_height_for_balance(self, node):
        if node:
            return node.height + 1
        return 0

    def get_balance(self, node):
        if not node:
            return 0
        return (self.get_height_for_balance(node.left) - self.get_height_for_balance(node.right))

    def right_rotate(self, node):
        print('right rotate')
        newroot = node.left
        newroot_og_right = newroot.right
        newroot.right = node
        newroot.right.left = newroot_og_right
        if node.value == self.head.value:
            self.head = newroot
        if not node.left and not node.right:
            node.height = 0
        else:
            node.height = 1 + max(self.get_height(node.left),
                                  self.get_height(node.right))
        newroot.height = 1 + \
            max(self.get_height(node.left), self.get_height(node.right))
        return newroot

    def left_rotate(self, node):
        print('left rotate')
        newroot = node.right
        newroot_og_left = newroot.left
        newroot.left = node
        newroot.left.right = newroot_og_left
        if node.value == self.head.value:
            self.head = newroot
        if not node.left and not node.right:
            node.height = 0
        else:
            node.height = 1 + max(self.get_height(node.left),
                                  self.get_height(node.right))
        newroot.height = 1 + \
            max(self.get_height(node.left), self.get_height(node.right))
        return newroot

    def insert(self, value, node="first"):
        if node == "first":
            node = self.head
        elif not node:
            return Node(value)

        if value < node.value:
            node.left = self.insert(value, node=node.left)
        elif value > node.value:
            node.right = self.insert(value, node=node.right)
        else:
            return "value already exists in tree"
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        return node

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def delete_node(self, value, node='first'):
        if node == 'first':
            node = self.head
        if not node:
            return node
        elif value > node.value:
            node.right = self.delete_node(value, node=node.right)
        elif value < node.value:
            node.left = self.delete_node(value, node=node.left)
        else:
            if not node.right:
                tempnode = node.left
                node = None
                return tempnode
            if not node.left:
                tempnode = node.right
                node = None
                return tempnode
            temp = self.get_min_value_node(node.right)
            node.value = temp.value
            node.right = self.delete_node(temp.value, node.right)

        if not node.left and not node.right:
            node.height = 0
        else:
            node.height = 1 + max(self.get_height(node.left),
                                  self.get_height(node.right))

        balance = self.get_balance(node)
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        return node
        # if value > node.value:
        #     if node.right.value == value:
        #         if not node.right.right and not node.right.left:
        #             del node.right
        #         elif node.right.right and node.right.left:
        #             newroot = node.right.right
        #             newroot.left = node.right.left
        #             node.right = newroot
        #         else:
        #             if node.right.right:
        #                 newroot = node.right.right
        #             if node.right.left:
        #                 newroot = node.right.left
        #             node.right = newroot
        #     self.delete_node(value, node.right)
        # elif value < node.value:
        #     self.delete_node(value, node.left)
        # else:
        #     del node

    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return "Node not found"


bst = AVLTree(4)
bst.insert(3)
bst.insert(2)
bst.level_order_traversal()
print("level order traversal")
bst.insert(1)
bst.level_order_traversal()
print("level order traversal")
bst.insert(5)
bst.level_order_traversal()
print("level order traversal")
bst.insert(9)
bst.in_order_traversal()
print('in oreder traversal')
bst.level_order_traversal()
# bst.level_order_traversal_height()
print("level order traversal")
bst.insert(6)
bst.level_order_traversal()
print("level order traversal")
bst.insert(7)
bst.level_order_traversal()
print("level order traversal")
bst.insert(12)
bst.level_order_traversal()
print("level order traversal")
bst.insert(15)
bst.level_order_traversal()
print("level order traversal")
bst.insert(18)
bst.level_order_traversal()
print("level order traversal")
bst.insert(21)
bst.level_order_traversal()
print("level order traversal")
bst.insert(24)
bst.level_order_traversal()
print('fin')

print(bst.search(5))
print(bst.search(10))

bst.delete_node(15)
print("level order traversal")
bst.level_order_traversal()

bst.delete_node(18)
print("level order traversal")
bst.level_order_traversal()

bst.delete_node(12)
print("level order traversal")
bst.level_order_traversal()

bst.delete_node(21)
print("level order traversal")
bst.level_order_traversal()

bst.delete_node(9)
print("level order traversal")
bst.level_order_traversal()

bst.delete_node(24)
print("level order traversal")
bst.level_order_traversal()
