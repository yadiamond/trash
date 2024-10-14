def lens(list):
    if list == []:
        return 0  
    else:
        return 1 + lens(list[1:])
print(lens([1, 2, 3, 4, 5]))

