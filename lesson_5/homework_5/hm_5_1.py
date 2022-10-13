# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
#
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
#
# out
# The data is incorrect

from random import sample

def rand_lst(count: int, wrd: str = 'абв'):
    return " ".join("".join(sample(wrd, 3)) for _ in range(count))

lst = rand_lst(int(input("Input number of words: ")))
print(lst)

new_lst = list(filter(lambda x: 'абв' not in x, lst.split(' ')))
print(' '.join(new_lst))
