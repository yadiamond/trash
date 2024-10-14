def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        x = list.pop(-1)
        return x + sum(list)
print(sum([2, 4, 6]))