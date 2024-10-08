#У Алисы сегодня день рождения, и она хочет угостить своих одноклассников конфетами. В магазине, в который она успеет зайти перед школой, есть сладости двух видов: шоколадные и карамельные. Они продаются наборами по 3 штуки, причем в упаковке есть конфеты каждого из двух
# видов (то есть в одной упаковке лежат две конфеты одного вида и одна конфета другого вида).
# По внешнему виду упаковки нельзя понять, какие конфеты лежат внутри.
# Чтобы никого не обидеть, всем в классе нужно раздать конфеты одного вида, а оставшиеся
# девочка заберёт домой. Алисе нужно собираться в школу, поэтому она попросила вас посчитать,
# какое минимальное число упаковок нужно купить, чтобы конфет хватило на всех.
# Формат входных данных
# В единственной строке задано число n (1 6 n 6 109
# ) — количество человек в классе.
# Формат выходных данных
# Выведите единственное число — количество упаковок, которое должна купить Алиса.

n = int(input())

if n % 3 == 0:
    print(n // 2 * 3)
else:
    print(n // 2 * 3 + 1)