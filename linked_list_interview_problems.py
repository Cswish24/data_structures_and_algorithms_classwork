# Create a linked list class

from ast import Raise
from random import randint


class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class SinglyLinkedlist():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        if self.head == None:
            return "Empty"
        position = self.head
        while position:
            yield position
            position = position.next

    def __len__(self):
        length = 0
        position = self.head
        while position:
            length += 1
            position = position.next
        return length

    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)

    def __getitem__(self, subscript):

        if self.head == None:
            return "Empty list"
        if isinstance(subscript, slice):
            node = self.head
            alist = []
            for i in range(subscript.stop):
                if i >= subscript.start and i < subscript.stop:
                    alist.append(node)
                if node == None:
                    raise IndexError()
                node = node.next
            return alist
        else:
            node = self.head
            for i in range(subscript + 1):
                if i == subscript:
                    return node
                if node.next == None:
                    raise IndexError()
                node = node.next

    def insert(self, value, position=-1):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node

        else:
            if position == 0:
                node.next = self.head
                self.head = node
            elif position == -1:
                self.tail.next = node
                self.tail = node

    def generate_random(self, n, max, min):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insert(randint(min, max))
        return self

    # def remove_duplicates(self):
    #     aset = {self.head.value}
    #     node = self.head
    #     while node.next:
    #         if node.next.value in aset:
    #             node.next = node.next.next
    #             continue
    #         else:
    #             aset.add(node.next.value)
    #         node = node.next

    def remove_duplicates(self):
        current_node = self.head
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current_node = current_node.next

    def search_value(self, target):
        if self.head == None:
            return "Empty list"
        for x in self:
            if x.value == target:
                print(f"List contains {target}")
                return x
        print(f"{target} not found")
        return None

    def search_index(self, index):
        if self.head == None:
            return "Empty list"
        node = self.head
        for i in range(index + 1):
            if i == index:
                return node
            if node.next == None:
                raise IndexError()
            node = node.next

    def partition(self, value):
        if self.head == None:
            return "Empty list"
        node = Node(self.search_value(value).value)
        newll = SinglyLinkedlist()
        newll.head = node
        newll.tail = node
        for h in self:
            newnode = Node(h.value)
            if h.value < value:
                newnode.next = newll.head
                newll.head = newnode
            elif h.value > value:
                newll.tail.next = newnode
                newll.tail = newnode
            else:
                pass
        return newll


def join_number(ll):
    combo = 0
    digit = 1
    for x in ll:
        combo += x.value * digit
        digit *= 10
    return combo


def sum_of_2_lists(ll1, ll2):
    return join_number(ll1) + join_number(ll2)


def int_to_ll(integer):
    ll = SinglyLinkedlist()
    string = str(integer)
    for c in string:
        newnode = Node(int(c))
        if ll.head == None:
            ll.head = newnode
            ll.tail = newnode
        else:
            newnode.next = ll.head
            ll.head = newnode
    return ll


sll = SinglyLinkedlist()
sll2 = SinglyLinkedlist()
sll.generate_random(3, 6, 1)
print(sll)
# sll.remove_duplicates()
# print(sll)
# target_node = sll.search_value(6)
# print(target_node.next)
# print(sll.search_index(5))
# print(sll[3])
# print(sll[1:3])
# for t in sll[1:5]:
#     print(t.value)
# print(sll.partition(4))
sll2.generate_random(3, 6, 1)
print(sll2)
print(sum_of_2_lists(sll, sll2))
athing = int_to_ll(sum_of_2_lists(sll, sll2))
print(athing)


