# Последовательностью Фибоначчи называется
# последовательность чисел a0 , a1 , ..., an , ..., где 
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(n):
#     if n in [0,1]:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input("Введите число: "))
# print(fib(n))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
n = int(input("Введите число: "))
print(fib(n))