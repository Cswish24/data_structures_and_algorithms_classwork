

from math import sqrt, ceil


def bubble_sort(iterable):
    for i in range(len(iterable)-1):
        k = 0
        j = 1
        while j < len(iterable) - i:
            if iterable[k] > iterable[j]:
                temp = iterable[k]
                iterable[k] = iterable[j]
                iterable[j] = temp
            k += 1
            j += 1


def selection_sort(iterable):
    for i in range(len(iterable) - 1):
        smallest_number = iterable[i]
        for k in range(i+1, len(iterable)):
            if iterable[k] < smallest_number:
                smallest_number = iterable[k]
                index = k
        temp = iterable[i]
        iterable[i] = iterable[index]
        iterable[index] = temp


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


def bucket_sort(arr):
    buckets = round(sqrt(len(arr)))
    listoflists = []
    for i in range(buckets):
        listoflists.append([])
    for num in arr:
        order = ceil((num * buckets / max(arr)))
        listoflists[order-1].append(num)
    for j in range(buckets):
        listoflists[j] = insertion_sort(listoflists[j])
    for k in range(1, len(listoflists)):
        listoflists[0].extend(listoflists[k])
    return listoflists[0]


def merge(arr, l, r, m):

    n1 = m - l + 1
    n2 = r - m

    leftlist = [0] * n1
    rightlist = [0] * n2

    for i in range(0, n1):
        leftlist[i] = arr[l + i]

    for j in range(0, n2):
        rightlist[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if leftlist[i] <= rightlist[j]:
            arr[k] = leftlist[i]
            i += 1
        else:
            arr[k] = rightlist[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = leftlist[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = rightlist[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr, l, r):
    if l < r:
        m = (l + (r-1))//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, r, m)
    return arr


def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)
    swap(arr, pivot_index, swap_index)
    return swap_index


def quicksort(arr, pivot_index, end_index):
    if end_index - pivot_index > 1:
        swap_index = pivot(arr, pivot_index, end_index)
        quicksort(arr, pivot_index, swap_index-1)
        quicksort(arr, swap_index + 1, end_index)
    else:
        return


sortee = list((5, 4, 7, 3, 2, 10, 12, 1))


print(sortee)
# bubble_sort(sortee)
# selection_sort(sortee)
print("space")
# print(insertion_sort(sortee))
# print(bucket_sort(sortee))
# print(merge_sort(sortee, 0, len(sortee)-1))
quicksort(sortee, 0, len(sortee)-1)


print("space")
print(sortee)
