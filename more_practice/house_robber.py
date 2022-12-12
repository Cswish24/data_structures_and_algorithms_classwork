# understand/ a robber can only rob every other house with know values. put the known values of houses into an array.
# ex. house array = [6, 7, 1, 30, 8, 2, 4]
# break down/   if value of (index + 1) > index + (index +2) then count skip to index +1

def robber(alist, index):
    if index == 2:
        return max(alist[1], alist[0])
    elif index == 1:
        return alist[0]
    rob_house = alist[index-1] + robber(alist, index-2)
    skip_house = robber(alist, index-1)
    return max(rob_house, skip_house)


houses = [6, 7, 1, 30, 8, 2, 4]

print(robber(houses, len(houses)))


def robber_td(alist, index, dict={}):
    if index == 2:
        return max(alist[1], alist[0])
    elif index == 1:
        return alist[0]
    if index in dict:
        return dict[index]
    rob_house = alist[index-1] + robber(alist, index-2)
    skip_house = robber(alist, index-1)
    dict[index] = max(rob_house, skip_house)
    return dict[index]


print(robber_td(houses, len(houses)))


def robber_dt(alist):
    alist.append(0)
    alist.append(0)
    i = 0
    total = 0
    while i < len(alist)-1:
        if alist[i] + alist[i+2] > alist[i+1]:
            total += alist[i]
            i += 2
        else:
            i += 1
    return total


print(robber_dt(houses))
