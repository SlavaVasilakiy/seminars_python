# 3. Задайте последовательность чисел. Напишите программу, которая выведет
#    список неповторяющихся элементов исходной последовательности в том же порядке.

# spisok = [5, 6, 8, 5, 8, 10, 5]
# print(spisok)
# novii_spisok = []
# for i in spisok:
#     count = 0
#     while count < len(spisok):
#         if i == spisok[count] and count != spisok.index(i):
#             count = 0
#             break
#         count += 1
#     else:
#         novii_spisok.append(i)
#         count = 0
#
# print(novii_spisok)

# spisok = ["a", "a", "c", "f", "g", 'g', 'j']
# print(spisok)
# novii_spisok = []
#
# for i in spisok:
#     if spisok.count(i) == 1:
#         novii_spisok.append(i)
#
# print(novii_spisok)

spisok = ["a", "a", "c", "f", "g", 'g', 'j']
print(spisok)

print(list(filter(lambda i: spisok.count(i) == 1, spisok)))

