# Айвар учится в восьмом классе. Он всерьез увлекается двумя школьными предметами –
# геометрией и технологией. Сегодня он решает геометрический этюд. Из проволоки Айвар вырезал
# три прямолинейных отрезка длиной a, b и c сантиметров соответственно. А из этих трех кусочков
# проволоки Айвар формирует на столе треугольник. Далее он совершает "события". За одно событие
# Айвар укорачивает каждый кусочек проволоки (т.е. каждую из сторон треугольника) на 1 см и вновь
# пытается сложить из таких укороченных кусочков проволоки треугольник. Спустя какое
# минимальное количество событий из имеющихся кусочков проволоки уже нельзя будет сложить
# треугольник?
# Формат входных данных:
# На вход программе подаются три натуральных числа a, b и c (1 ≤ a, b, c ≤ 109
# ). Гарантируется,
# что из отрезков заданной длины треугольник составить можно.
# Формат выходных данных:
# В качестве результата Ваша программа должна вывести одно целое число: минимальное
# количество событий, после которых, из имеющихся кусочков проволоки уже нельзя будет сложить
# треугольник.

a = int(input())
b = int(input())
c = int(input())

maxn = max(a, b, c)

print(a+b+c-maxn-maxn)