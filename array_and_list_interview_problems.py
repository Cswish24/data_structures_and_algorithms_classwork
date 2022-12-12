list1 = [2, 6, 3, 9, 11]
target = 9


# def sumfrompairs(arr, tar):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == tar:
#                 print((arr[i], arr[j]))


# sumfrompairs(list1, target)


# # def sumfrompairs2(arr, tar):
# #     for i in range(len(arr)):
# #         if arr[i]

# def findnumberlinear(arr, tar):
#     for i in range(len(arr)):
#         if arr[i] == tar:
#             print(i)


# findnumberlinear(list1, 6)

# counter = 0


# def findnumberbinary(arr, tar):
#     # global counter
#     # counter += 1
#     # print(counter)
#     print(arr[len(arr)//2])
#     print(arr)
#     if arr[len(arr)//2] == tar:
#         print(True)
#         print(len(arr)//2)
#         return len(arr)//2
#     elif arr[len(arr)//2] < tar:
#         findnumberbinary(arr[len(arr)//2: len(arr)], tar)
#     elif arr[len(arr)//2] > tar:
#         findnumberbinary(arr[0: len(arr)//2], tar)


# sorted_list = [1, 2, 3, 4, 6, 12, 15, 66, 77, 88, 99]

# print(findnumberbinary(sorted_list, 4))

# def maxproduct(arr):
#     max_product = 0
#     max_loc = None
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             product = arr[i]*arr[j]
#             if product > max_product:
#                 max_product = product
#                 max_loc = (i, j)
#     print((max_product, max_loc))


# maxproduct(list1)


# def islistunique(arr):
#     empty_list = []
#     for i in arr:
#         for j in empty_list:
#             if i == j:
#                 print("not unique")
#                 return
#         empty_list.append(i)
#     print("unique")
#     return


# islistunique(list1)
# list2 = [1, 2, 3, 4, 4, 5, 6, 7, 8]
# islistunique(list2)


# list1 = [1, 3, 5, 7, 11]
# list2 = [3, 1, 7, 11, 5]
# list3 = [3, 1, 7, 12, 11]


# def ispermutation(arr1, arr2):
#     if sorted(arr1) == sorted(arr2):
#         print(True)
#     else:
#         print(False)


# def sortfunc(arr):
#     arrsorted = []
#     for i in range(len(arr)):
#         max_v = arr[i]
#         for j in range(i, len(arr)):
#             if arr[j] > max_v:
#                 arr[j] = max_v
#                 pos = j
#         arrsorted.append(arr.pop(pos))
#     print(arrsorted)


# ispermutation(list1, list2)
# ispermutation(list1, list3)
# sortfunc(list2)


# dict1 = {"akey": 24, "bkey": 25}

# if "akey" in dict1:
#     print('it works')

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

print(sum(list((init_tuple_a + init_tuple_b))))
