# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# Примеры:

# o 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4,


a = abs(int(input('N = ')))
for i in range(-a, a + 1):
    print(i, end=' ')