# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
from random import randint
n = int(input("Введите количество монет: "))
count = 0
gerb = 0
reshka = 0
while count < n:
    side = randint(0,1)
    if side == 0:
        reshka += 1
    else:
        gerb += 1
    print(side, end=" ")
    count += 1
if reshka > gerb:
    print(f"Минимальное количество монет необходимо перевернуть {gerb}")
elif reshka < gerb:
    print(f"Минимальное количество монет необходимо перевернуть {reshka}")
else:
    print(f"Минимальное количество монет необходимо перевернуть {gerb}")