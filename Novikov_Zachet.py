#Тема: Функции map, filter, reduce, any, all.
        
#Задача 1. Дан список температур в градусах Цельсия или Фаренгейта. Преобразовать
#их в соответствующие температуры в градусах Фаренгейта или Цельсия (с использованием
#map). Источник: https://realpython.com/python-map-function/

def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f):
    return (f - 32) * 5 / 9

#Перевод в градусы Фаренгейта:
celsius_temps = [100, 40, 80, -10, -20]
print(list(map(to_fahrenheit, celsius_temps)))

#Перевод в градусы Цельсия:
fahr_temps = [212, 104, 176]
print(list(map(to_celsius, fahr_temps)))


#Задача 2. Найти все простые числа в заданном интервал (с использованием filter).
#Источник: https://realpython.com/python-filter-function/

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#Нахождение простых числе в диапозонах от 1 до 50 и от 20 до 70:
print(list(filter(is_prime, range(1, 51))))
print(list(filter(is_prime, range(20, 71))))


#Задание 3. Написать функцию, которая вычисляет сумму чисел в списке и выводит на
#экран эквивалентные математические операции (с использованием reduce).
#Источник: https://realpython.com/python-reduce-function/

from functools import reduce

def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

#Нахождение суммы чисел в списках:
numbers1 = [0, 1, 2, 3, 4]
numbers2 = [3, 4, 7, 11, -3]
print(reduce(my_add, numbers1))
print(reduce(my_add, numbers2))



















