# # Найти большее число из двух

# # a = int(input("Число A: "))

# # b = int(input("Число Б: "))

# # if a > b:
# #     print(f"наибольшее чило А = {a}")
# # elif a == b:
# #     print(f"Оба числа равны")
# # else:
# #     print(f"наибольшее чило Б = {b}")


# a = int(input("Число A: "))
# n = ['no', 'yes']
# print(n[a%2==0])
# print(a%2==0)

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# import math
n = int(input("Сколько километров машина проезжает за день: "))
m = int(input("Длинна маршрута: "))
# output = m / n
# output = math.ceil(output)
# print(output)


s = (m + n - 1) // n
print(s)