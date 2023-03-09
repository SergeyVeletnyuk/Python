# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('введите число: '))
i = 0
result = 0
while result < n:
    if result < n:
        result = 2 ** i
        i += 1
        
        if result > n:
            break
    print(result)