# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

n = int(input('input number of elements: '))
n_list = list(range(n))
list_len = len(n_list)
print(n_list)

for i in range(list_len):
    pos_1 = randrange(list_len)
    pos_2 = randrange(list_len)
    n_list[pos_1], n_list[pos_2] = n_list[pos_2], n_list[pos_1]

print(n_list)
