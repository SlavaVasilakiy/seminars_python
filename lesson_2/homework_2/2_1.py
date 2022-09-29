# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

n = float(input('Input a number: '))
n_length = len(str(n)) - 1
m = int(n * 10 ** n_length)
print(m)
suma = 0
while m > 0:
    digit = m % 10
    suma = suma + digit
    m = m // 10
print(suma)