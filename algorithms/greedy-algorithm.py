# # Задача: Имеется учебный класс. Нужно провести как можно больше уроков. Дается список уроков отсортированный по времени. Сначала идут уроки которые раньше остальных закончатся
from datetime import time

def make_lessons(lessons):
    ans = []
    current = lessons.pop(0)
    ans.append(current)
    while current[1] < lessons[-1][1]:
        for i in range(len(lessons)):
            if lessons[i][0] >= current[1]:
                current = lessons.pop(i)
                ans.append(current)
                break
    return ans