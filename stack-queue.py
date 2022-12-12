# class Stack():
#     def __init__(self, inner_max_size, outer_max_size):
#         self.inner_max_size = inner_max_size
#         self.outer_max_size = outer_max_size
#         self.stack_outer = [[] for x in range(outer_max_size)]
#         print(self.stack_outer)

#     def __str__(self):
#         return f"{self.stack_outer}"

#     def push(self, value):
#         if isinstance(value, list):
#             if len(self.stack_outer) < self.outer_max_size:
#                 self.stack_outer.append(value)
#             else:
#                 return "Outer Stack is full"
#         else:
#             for lst in self.stack_outer:
#                 if len(lst) < self.inner_max_size:
#                     lst.append(value)
#                     return
#             print("All Stacks full")

#     def pop(self):
#         for i in range(self.outer_max_size - 1, 0, -1):
#             if self.stack_outer[i]:
#                 return self.stack_outer[i].pop()

#     def pop_stack(self, stack_number):
#         if stack_number < self.outer_max_size:
#             if self.stack_outer[stack_number]:
#                 return self.stack_outer[stack_number].pop()
#             else:
#                 return "Stack Is empty"
#         else:
#             return "Stack number is not in range of stacks"

#     def push_stack(self, value, stack_number):
#         if stack_number < self.outer_max_size:
#             if len(self.stack_outer[stack_number]) < self.inner_max_size:
#                 self.stack_outer[stack_number].append(value)
#             else:
#                 return "Stack Is full"
#         else:
#             return "Stack number is not in range of stacks"


# stack = Stack(3, 3)

# stack.push(2)
# stack.push(2)
# stack.push(2)
# stack.push(2)
# stack.push(2)
# stack.push(2)
# stack.push(2)
# stack.push(2)
# stack.push(2)
# stack.push(2)
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop_stack(0)
# stack.push_stack(5, 2)
# print(stack)
# stack.push(1)
# print(stack)
# stack.push(4)
# print(stack)


# Stack as queue

# class Stack():
#     def __init__(self):
#         self.stack = []
#         self.queue = []

#     def __str__(self):
#         return f"{self.stack}, {self.queue}"

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.queue:
#             self.queue.pop()
#         else:
#             for i in range(len(self.stack)):
#                 self.queue.append(self.stack.pop())
#             self.queue.pop()


# stack = Stack()
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack)
# stack.pop()
# print(stack)
# stack.push(5)
# stack.push(6)
# stack.push(7)
# stack.pop()
# print(stack)
# stack.pop()
# stack.pop()
# print(stack)

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        return "->".join([str(node.value) for node in self])

    def push(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        node = self.head
        self.head = self.head.next
        return node


class AnimalShelter():
    def __init__(self):
        self.queue = linkedlist()

    def __str__(self):
        return str(self.queue)

    def push(self, value):
        self.queue.push(value)

    def adopt(self, animal=None):
        if animal == "cat":
            node = self.queue.head
            while node:
                if node.value[0] == "cat":
                    if node is self.queue.head:
                        self.queue.head = node.next
                        self.queue.head.prev = None
                        return node
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        return node
                node = node.next

        elif animal == "dog":
            node = self.queue.head
            while node:
                if node.value[0] == "dog":
                    if node is self.queue.head:
                        self.queue.head = node.next
                        self.queue.head.prev = None
                        return node
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        return node
                node = node.next
        else:
            node = self.queue.head
            self.queue.head = node.next
            self.queue.head.prev = None
            return node


ll = AnimalShelter()

ll.push(("cat", "bruce"))
ll.push(("cat", "greely"))
ll.push(("cat", "junie"))
ll.push(("dog", "ginger"))
ll.push(("dog", "captain"))
print(ll)
ll.adopt("cat")
print(ll)
ll.adopt()
print(ll)
ll.push(("cat", "mickey"))
print(ll)
ll.adopt("dog")
print(ll)
