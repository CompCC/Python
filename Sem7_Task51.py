# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
# Ввод:                                    Вывод:
# values = [0, 2, 10, 6]                   same
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
#     print(‘different’)

def same_by(characteristic, objects):
    temp = characteristic(objects[0])
    for i in range(1, len(objects)):
        if characteristic(objects[i]) != temp:
           return False
    return True


values = [0, 2, 10, 6]                   
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')




def same_by(func, collection):
    return len(list(filter(func, collection))) == 0


values = [0, 2, 10, 6, 8, 12, 24, 1]
if same_by(lambda x: x % 2, values):
 print('same')
else:
 print('different')