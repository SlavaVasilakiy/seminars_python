# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# o 6 -> да

# o 7 -> да

# o 1 -> нет

num = int(input('Введите цифру дня недели: '))

if num == 1:
    print('Понедельник')
elif num == 2:
    print('Вторник')
elif num == 3:
    print('Среда') 
elif num == 4:
    print('Четверг')
elif num == 5:
    print('Пятница')
elif num == 6:
    print('Суббота - ВЫХОДНОЙ !')
elif num == 7:
    print('Воскресенье - ВЫХОДНОЙ !')
else:
    print('Это не день недели !')