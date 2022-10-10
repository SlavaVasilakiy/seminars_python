# 2. Дан список чисел. Создайте список, в который попадают числа,
#    описываемые возрастающую последовательность.
#    Порядок элементов менять нельзя.

from random import choices

def new_list (size):
    list_of_numbers = choices(range(1, size * 2), k = size)
    return list_of_numbers
n_list = new_list(10)
print(n_list)

def range_nums (new_list: list):
    my_list = []
    for i in range(len(new_list)):
        f = new_list[i]
        list_1 = [f]
        for k in range(i + 1, len(new_list)):
            if new_list[k] > f:
                f = new_list[k]
                list_1.append(f)
        if len(list_1) > 1:
            my_list.append(list_1)
    return my_list

print(range_nums(n_list))
