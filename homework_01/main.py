"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List, Union


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    my_list = []
    for numbers in args:
        my_list.append(numbers ** 2)
    return my_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    if number < 2:
        return False
    return True

def filter_numbers(my_list: List[int], text: str) -> Union[List[int], str]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]

    """

    if text == ODD:
        return list(filter(lambda x: x % 2 != 0, my_list))
    elif text == EVEN:
        return list(filter(lambda x: x % 2 == 0, my_list))
    elif text == PRIME:
        return list(filter(is_prime, my_list))
    else:
        return 'Error'


print(filter_numbers([0, 1, 2, 3, 4, 12, 17], PRIME))
