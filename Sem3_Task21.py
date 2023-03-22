# Напишите программу для печати всех уникальных значений в списке.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# list1=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# a = set()
# for i in list1:
#     for j in i:
#         a.add(i[j])
# print(a)

# a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#      {"VII": "S005"}, {" V ":" S009 "}, {" VIII":" S007 "}]
# s = set()
# for i in a:
#     s.add(*i.values())
# print(*s)

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] #список
print(data)
result_set = set()
for elem in data:
    for value in elem.values():
        result_set.add(value.strip())
print(result_set)