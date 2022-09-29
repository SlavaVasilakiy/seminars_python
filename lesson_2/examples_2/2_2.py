# 2. Создать список, длины n, значения формируются по формуле 3k + 1, где k принимает значения от 1 до n включительно.

n = []
count = int(input('Input count number: '))
for i in range(1, count + 1):
    n.append(3 * i + 1)
print(n)