class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsack_method(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    used_capacity = 0
    total_value = 0
    for i in items:
        if used_capacity + i.weight <= capacity:
            used_capacity += i.weight
            total_value += i.value

        else:
            capacity_left = capacity - used_capacity
            value = i.ratio * capacity_left
            used_capacity += capacity_left
            total_value += value

        if used_capacity == capacity:
            break
    print(f"Total value = {total_value}")


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
alist = [item1, item2, item3]

knapsack_method(alist, 50)
