# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
a = int(input('Введите первый элемент массива: '))
d = int(input('Введите разность м-у элементами: '))
n = int(input('Введиет кол-во элементов: '))
line_1 = []

for i in range(1,n+1):
    line_1.append(a + (i-1)*d)
print(*line_1)