# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input('input a number: '))
a = [round((1 + 1 / x) ** x) for x in range(1, n + 1)]
sum = 0
for i in a:
    sum = sum + i
print(f'{a} sum = {sum}')