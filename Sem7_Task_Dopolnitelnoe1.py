# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности 
# оставшихся чисел в одну строчку через пробел.

n = input('Введите последовательность чисел через пробел: ').split()
n = list(map(int, n))   # перевод из строковых данных в числовые

res = list(filter(lambda x: 100 > x > 10, n))
print(*res)


