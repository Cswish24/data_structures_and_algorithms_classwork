

class Heap():
    def __init__(self, max_size, min=True):
        self.max_size = max_size + 1
        if min:
            self.min = True
        else:
            self.min = False
        self.heap_size = 0
        self.heap = self.max_size * [None]

    def level_order_traversal(self):
        for i in range(1, self.heap_size + 1):
            print(self.heap[i])

    def get_heap_size(self):
        return self.heap_size

    def insert(self, value):
        if self.heap_size < self.max_size:
            self.heap[self.heap_size+1] = value
            self.heap_size += 1
            self.heapify()
        else:
            print('heap is full')

    def heapify(self, heap_slot='entry'):
        if heap_slot == "entry":
            heap_slot = self.heap_size
            if heap_slot == 1:
                return
        elif heap_slot == 1:
            return
        if self.heap[heap_slot] < self.heap[heap_slot//2]:
            print("swapping")
            temp = self.heap[heap_slot]
            self.heap[heap_slot] = self.heap[heap_slot//2]
            self.heap[heap_slot//2] = temp
            heap_slot = self.heap_size // 2
            self.heapify(heap_slot=heap_slot)

    def heapify_extract(self, index):
        left = index * 2
        right = (index*2) + 1
        if left == self.heap_size:
            if self.heap[index] > self.heap[left]:
                temp = self.heap[index]
                self.heap[index] = self.heap[left]
                self.heap[left] = temp
                index = left
            else:
                return

        elif right <= self.heap_size:
            if self.heap[index] > self.heap[left] or self.heap[index] > self.heap[right]:
                if self.heap[left] > self.heap[right]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[right]
                    self.heap[right] = temp
                    index = right
                else:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left]
                    self.heap[left] = temp
                    index = left
            else:
                return
        else:
            return
        self.heapify_extract(index)

    def extract(self):
        temp = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap[self.heap_size] = None
        self.heap_size -= 1
        self.heapify_extract(1)
        return temp


heap = Heap(15)
heap.insert(40)
heap.insert(30)
heap.level_order_traversal()
heap.insert(20)
heap.level_order_traversal()
heap.insert(10)
heap.level_order_traversal()
heap.insert(5)
heap.level_order_traversal()
heap.extract()
print('extracting')
heap.level_order_traversal()
heap.extract()
print('extracting')
heap.level_order_traversal()
heap.extract()
print('extracting')
heap.level_order_traversal()
heap.extract()
print('extracting')
heap.level_order_traversal()
heap.extract()
print('extracting')
heap.level_order_traversal()
heap.extract()
print('extracting')
heap.level_order_traversal()
