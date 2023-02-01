# Задача 3: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# a = int(input('Введите шестизначный номер билета '))
# result1 = a // 1000
# result2 = a % 1000
# print(result1, result2)
# value1= result1%10
# value2 = (result1%100)//10
# value3 = (result1%1000)//100

# value4= result2%10
# value5 = (result2%100)//10
# value6 = (result2%1000)//100
# if value1 + value2 + value3 == value4 + value5 + value6:
#     print('ура!!! Это счастливый билет!!')
# else:
#     print('Этот билет к сожалению не счастливый')


A =  input('введите шестизначный номер билета: ')
temp = []
# while len(A) != 6:
#     A = input('введите шестизначный номер билета: ')
while len(A:=input('введите шестизначный номер билета: ')) !=6:
    print('ошибка')
for i in range(len(A)):
    temp.append(A[i])
print(temp)


result1 = 0
result2 = 0
i = 0
result1 = (sum((int(temp[i]) for i in range(0, 3))))
result2 = (sum(int(temp[i]) for i in range(3, int(len(temp)))))
print(result1, result2)

if result1 == result2:
    print('Ехууу! У меня счастливый билет!!')
else:
    print('может в следующий раз повезет =(')
