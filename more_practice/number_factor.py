# given N , find the number of ways to express n as a sum of 1, 3, and 4

# step 1, understand the problem
# changing the order of addition of the same numbers does indeed count as a unique expression of n

# step 2, Examples
# if N = 4 then (1,3) (3,1) (1,1,1,1) and (4) are the expressions of 4, there is a total of 4 expressions for N = 4

# step 3, break it down
# for div and conq we need
# func(n, tot =0):
#   if n_cumulative equals n
#     return 1
# if n_cumulative is less than n
#     func n + (1 and 2 and 4)
# else return 0

# def num_fac(n, n_cumulative=0):
#     if n_cumulative == n:
#         return 1
#     elif n_cumulative < n:
#         a = num_fac(n, n_cumulative + 3)
#         b = num_fac(n, n_cumulative + 4)
#         c = num_fac(n, n_cumulative + 1)
#     else:
#         return 0
#     return a + b + c

def num_fac(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        a = num_fac(n-1)
        b = num_fac(n-3)
        c = num_fac(n-4)
        return a + b + c


# print(num_fac(35))


def num_fac_td(n, dict={}):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n in dict:
            return dict[n]
        else:
            dict[n-1] = num_fac_td(n-1)
            dict[n-3] = num_fac_td(n-3)
            dict[n-4] = num_fac_td(n-4)
            return dict[n-1] + dict[n-3] + dict[n-4]


print(num_fac_td(9))


def num_fac_dt(n):
    alist = [1, 1, 1, 2]
    for i in range(4, n+1):
        alist.append(alist[i - 1] + alist[i - 3] + alist[i-4])
    return alist[n]


print(num_fac_dt(9))
