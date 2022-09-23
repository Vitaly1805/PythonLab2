from random import random
from sys import getsizeof


def get_random_list():
    for _ in range(1000):
        yield random()


arr1 =  [random() for i in range(1000)]

arr2 = get_random_list()

counter = 0

for i in arr2:
    counter += 1

    if counter == 1:
        print('Первый элемент последовательности = ', i)

    if counter == 2:
        print('Второй элемент последовательности = ', i)
        break

print('Выделено под список: ', getsizeof(arr1))
print('Выделено под генератор: ', getsizeof(arr2))