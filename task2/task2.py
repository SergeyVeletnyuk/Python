# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем
# Петя и Сережа вместе?
# 6-> 1 4 1
# 24-> 4 16 4
# 60 - > 10 40 10

# s = int(input('Введите количество журавликов сколько сделали Катя, Петя и Сережа вместе '))
# Sergey = 0
# Petya = 0
# Katya = 0
# while Sergey + Petya + Katya != s:
#     Sergey = Sergey + 1
#     Petya = Petya + 1
#     Katya = (Sergey + Petya)*2  
# print(Sergey, Petya, Katya)


# ////
# s = int(input('Введите количество журавликов сколько сделали Катя, Петя и Сережа вместе '))
# x + x + (x+x)*2 = s
# s = 6x
# x = s/6
# Petya = s//6
# Katya = (s//6)*4
# Sergey = s//6
# if Petya + Katya + Sergey == s:
#     print(Petya,Katya, Sergey)
# else:
#     print('Ровное кол-во не получается , введите другое число')