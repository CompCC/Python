# Стоимость строки

# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 
# 60
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести стоимость строки.

# Тестовые данные 
# Sample Input 1:
# Привет, как дела?!
# Sample Output 1:
# 10 р. 80 коп.
# Sample Input 2:
# Тимур - лучший математик на свете!!
# Sample Output 2:
# 21 р. 0 коп.

string = input("Введите посчитываемую строку: ")
s = len(string)
res = s * 60
print(f"Стоимость строки составит {res//100} р. {res%100} коп.")