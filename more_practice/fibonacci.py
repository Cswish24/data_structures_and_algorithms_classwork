
#divide and conquer
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


# fibby = fib(35)
# print(fibby)

# dynamic top down


def fib_td(n, dict={}):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in dict:
        return dict[n]
    dict[n] = fib_td(n-1) + fib_td(n-2)
    return dict[n]


fibby_td = fib_td(10)
print(fibby_td)


def fib_dt(n):
    alist = [0, 0, 1]
    for i in range(3, n+1):
        alist.append(alist[i-1] + alist[i-2])
    return alist[n]


fibby_dt = fib_dt(10)

print(fibby_dt)
