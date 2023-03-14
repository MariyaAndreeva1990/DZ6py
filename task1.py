"""
Задача 26: Напишите программу, которая на вход принимает два числа
 A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

def extent_of_number(number, extent):
    if (extent == 1):
        return number
    if (extent != 1):
        return (number * extent_of_number(number, extent - 1))
num = int(input("Введите число: "))
ext = int(input("Введите степень: "))
print(f" A = {num}; B = {ext} -> {extent_of_number(num, ext)}")