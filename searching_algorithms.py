def linear_search(arr, value):
    for i in arr:
        if i == value:
            return i


def binary_search(arr, value):
    end = len(arr)-1
    middle = end//2
    start = 0
    if arr[middle] == value:
        return middle
    elif arr[end] == value:
        return end
    elif arr[start] == value:
        return start
    while middle > start:
        if value == arr[middle]:
            return middle
        elif value < arr[middle]:
            end = middle
            middle = (start + end)//2
        else:
            start = middle
            middle = (end + start)//2
    return "value not found"


arr = [1, 3, 4, 7, 8, 10, 34, 55, 66, 77]
print(binary_search(arr, 90))
