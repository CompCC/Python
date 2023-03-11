# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticket = int(input("Введите 6-ти значный номер билета: "))
n1 = ticket//1000
n2 = ticket%1000
sum1 = 0
sum2 = 0
while n1>0:
    x = n1%10
    sum1 += x
    n1 = n1//10
while n2>0:
    x = n2%10
    sum2 += x
    n2 = n2//10
if sum1==sum2:
    print("Ваш билет счастливый!")
else:
    print("Ваш билет не счастливый.")