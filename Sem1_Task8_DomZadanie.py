# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("Введите размер шоколадки по вертикали: "))
m = int(input("Введите размер шоколадки по горизонтали: "))
k = int(input("Сколько нужно отломить долек? "))
if k < m*n and (k % m == 0 or k % n == 0):
    print("Можно")
else:
    print("Нельзя")