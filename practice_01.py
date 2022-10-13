# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
#
# in
# 424
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

from random import randint
my_list = [randint(20, 100) for i in range(20)]
print(my_list)
numbers = list(filter(lambda i: not i % 20 or not i % 21, my_list))
print(numbers)

# my_list = []
# for i in range(20):
#     numbs = randint(20, 100)
#     my_list.append(numbs)
# print(my_list)
#
# new_list = []
# for k in my_list:
#     if k % 20 == 0 or k % 21 == 0:
#         new_list.append(k)
#         k += 1
# print(new_list)
