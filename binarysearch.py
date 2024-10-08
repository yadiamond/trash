def binarysearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        target = list[mid]
        if target == item:
            return mid
        elif target > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

list = [1, 2, 3, 4]
print(binarysearch(list, 3))    