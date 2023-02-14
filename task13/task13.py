# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A = int(input('A: '))
B = int(input('B: '))
def result(A,B):
    if B == 0:
        return 1
    elif B == 1:
        return A
    return A*result(A,B-1)

print(result(A,B))

