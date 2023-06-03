# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Enter A: "))
b = int(input("Enter B: "))


def powRec(a, b):
    if b < 1:
        return 1
    return a * powRec(a, b - 1)


print(f"PowRec = {powRec(a, b)}")


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2 -> 4

a = int(input("Enter A: "))
b = int(input("Enter B: "))


def summa(a, b):
    if a == 0:
        return b
    return summa(a - 1, b + 1)


print(f"Summ = {summa(a, b)}")
