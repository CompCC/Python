# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

from math import pow
n = int(input("Введите максимальную степень 2х: "))
s = 1
res = 0
while res < n:
    res = int(pow(2, s))
    if res > n:
        break
    print(res)
    s += 1
    