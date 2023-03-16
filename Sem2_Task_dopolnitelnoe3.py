# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#     *Пример:*

#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

n = int(input("Введите число: "))
res = str()
while n > 0:
    temp = n % 2
    if temp == 0:
        res += str(0)
    else:
        res += str(1)
    n = n//2
def revers_string(res):  #функция переворацивания строки с помощью среза
    return res[::-1]
print(revers_string(res))
