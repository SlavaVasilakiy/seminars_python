# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
num = int(input('input number of elements: '))
a = []
for i in range(-num, num + 1):
    a.append(i)
print(a)
pos_1 = int(input('input position one: '))
pos_2 = int(input('input position two: '))
print(f'product of numbers on positions ({pos_1}) and ({pos_2}) = {a[pos_1 - 1] * a[pos_2 - 1]}')
