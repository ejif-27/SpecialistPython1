# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random


def gen_list(size, of, to):
    list_num = []

    for _ in range(size):
        list_num.append(random.randint(of, to))
    return list_num

print(gen_list(10, -60, 0))
