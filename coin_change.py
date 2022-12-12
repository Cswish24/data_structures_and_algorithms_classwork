def coin_change_alg(change):
    coins = {100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 0}
    while change != 0:
        for coin in coins.keys():
            if coin <= change:
                change -= coin
                coins[coin] += 1
                break
    return coins


change = coin_change_alg(236)
print(change)
