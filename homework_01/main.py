"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(in_number):
    # Я загуглил этот алгоритм, т.к. помнил, что точно есть
    # оптимизированный способ проверить, простое число или нет.
    # Логика в том, что есть определенное число, после которого
    # деления без остатка 100% не выйдет.
    # Это число — квадратный корень из проверяемого.
    # Чтобы не вляпываться во float от извлечения корня из in_number,
    # возвожу test_number в квадрат и сравниваю так
    
    if in_number == 1:
        return False

    test_number = 2
    while test_number**2 <= in_number:
        if in_number % test_number == 0:
            return False
        test_number += 1

    return True

def filter_numbers(test_list, filter_type=ODD):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == PRIME:
        return [number for number in test_list if is_prime(number)]
        
    elif filter_type == ODD:
        return list(filter(lambda n: n % 2 != 0, test_list))
        
    elif filter_type == EVEN:
        return [number for number in test_list if number % 2 == 0]
    
    return None