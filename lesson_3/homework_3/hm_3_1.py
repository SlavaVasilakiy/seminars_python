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

def SumOfNumbers(my_list):
    list_sum = 0
    for i in range(0, len(my_list), 2):
        list_sum = list_sum + my_list[i]
    return list_sum

print(SumOfNumbers(my_list))

