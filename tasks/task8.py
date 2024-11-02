s = input()
n = int(input())
x = {}
ans = s  # Начнем с исходной строки

# Чтение пар значений
for i in range(n):
    z = input().split()
    x[z[1]] = z[0]  # z[1] - кодовое слово, z[0] - его расшифровка

# Проходим по словарю и заменяем в ans
for code, replacement in x.items():
    ans = ans.replace(code, replacement)  # Заменяем все вхождения кодового слова на расшифровку

print(ans)
