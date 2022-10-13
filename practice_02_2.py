# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint
lst = [randint(1, 100) for i in range(randint(5, 10))]
print(lst)
print(sum([lst[i] for i in range(1, len(lst), 2)]))
