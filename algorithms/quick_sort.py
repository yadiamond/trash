#Задача: отсортировать список
def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        mid = len(list) // 2
        less = [list[i] for i in range(len(list)) if list[i] <= list[mid] and i != mid]
        greater = [i for i in list if i > list[mid]]
        return quick_sort(less) + [list[mid]] + quick_sort(greater)