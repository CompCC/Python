# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# k = int(input("Введите число сдвига списка: "))
# List_1 = [1, 2, 3, 4, 5]
# List_2 = []
# for i in range(k):
#     List_2.append(List_1[0])
#     List_1.pop(0)
# print(List_1+List_2)

# arr = [1, 2, 3, 4, 5]
# k = 4
# arr = arr[k:] + arr[:k]
# print(arr)

lst = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    lst.insert(0, lst.pop(-1))
print(lst)