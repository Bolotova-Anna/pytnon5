# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
def rec(a, b):
    if b == 0:
        a = 1
        return a
    n = rec(a,b-1) *a
    return n
a = int(input("введите число a: "))
b = int(input("введите число b: "))
print(rec(a,b))


