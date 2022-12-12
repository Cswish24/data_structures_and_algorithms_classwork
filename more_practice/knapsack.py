# find the maximum value of items with different weights and values that one can carry if only so much wieght can be carried.
# ex. (item, value, weight) (orange, 17, 2), (banana, 72, 5), (apple, 26, 1), (mango, 31, 3) max capacity = 7
# find max value ratios

def knapsack_problem(items, max_capacity, capacity=0, index=0):
    if index == len(items) or capacity >= max_capacity:
        return 0
    add_item = items[index][1] + knapsack_problem(
        items, max_capacity, capacity+items[index][2], index+1)
    skip_item = knapsack_problem(items, max_capacity, capacity, index+1)
    if max_capacity < capacity + items[index][2]:
        return skip_item
    else:
        return max(add_item, skip_item)


items = [("orange", 17, 2), ("banana", 72, 5),
         ("apple", 26, 1), ("mango", 31, 3)]

print(knapsack_problem(items, 7))


def knapsack_problem_td(items, capacity, index=0, dict={}):
    if index == len(items) or capacity <= 0:
        return 0
    key = (capacity*10)+index
    if key in dict:
        return dict[key]
    skipitem = knapsack_problem_td(items, capacity, index+1)
    if capacity < items[index][2]:
        return skipitem
    else:
        additem = items[index][1] + \
            knapsack_problem_td(items, capacity-items[index][2], index+1)
        dict[key] = max(additem, skipitem)
        return dict[key]


print(knapsack_problem_td(items, 7))


def knapsack_problem_dt(items, capacity, list=[]):

    # find maximum weight/value ratios, while weight < capacity, loop, put highest value ratio item first in loop, if item selected add
    # weight and value to knapsack then restart loop. if no items can fit in knapsack, else at end to break the loop

    # def knapsack_problem(items, max_capacity):
    #     knapsack = []
    #     for item in items:
    #         knapsack.append((item[0], 0, item[1]/item[2]))
    #     knapsack.sort(key=lambda x:x[3])
    #     knapsack[0][1] = max_capacity //
