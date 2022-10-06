# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
#
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randint

n = int(input('Input list range: '))
my_list = [randint(1, 10) for i in range(n)]
print(my_list)


def prod_pairs(my_list: list):
    res_list = []
    len_list = len(my_list)

    for k in range(len_list // 2):
        res_list.append(my_list[k] * my_list[len_list - k - 1])

    if len_list % 2:
        res_list.append(my_list[len_list // 2])
    return res_list


print(prod_pairs(my_list))
