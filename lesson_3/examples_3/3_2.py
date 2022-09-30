# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import choices

def new_list(n, word):
    n_list = []
    for i in range(n):
        a = choices(word, k = 3)
        n_list.append(''.join(a))
    return n_list

def list_search(s_list, key):
    if s_list.count(key) > 1:
        n = s_list.index(key)
        print(s_list.index(key, n + 1))
        print('Yes')
    else:
        print('-1')

result = new_list(15, 'abc')
print(result)
list_search(result, input('input search words: '))
