# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
#
# out
# [4, 2, 4, 9]
# 8

from random import randint

n = int(input('Input list range: '))
my_list = [randint(1, 10) for i in range(n)]
print(my_list)

# from random import sample


# def list_rand_nums(count: int):
#     if count < 0:
#         print("Negative value of list range!")
#         return []

#     rand_numbs = sample(range(1, count * 2), count)
#     return rand_numbs

def sum_of_numbers(rand_numbs: list):
    list_sum = 0
    for i in range(0, len(rand_numbs), 2):
        list_sum += rand_numbs[i]
    return list_sum

my_list = list_rand_nums(int(input('Input list range: ')))
print(my_list)
print(sum_of_numbers(my_list))
