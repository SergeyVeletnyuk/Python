# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2

# sum = 5
# proizvedenie = 6
# result = True
# while result:
#     value1 = int(input('введите число: '))
#     value2 = int(input('введите второе число: '))
#     if value1 + value2 == sum and value1 * value2 == proizvedenie:
#         print()
#         print(f'ура!!! ты отгадал цифры которые я загадал')
#         print(f'{value1}, {value2}')
#         result = False
#     else:
#         print(f'попробуй еще раз \nсумма = {sum} \nпроизведение = {proizvedenie}')




a = int(input('сумма = '))
b = int(input('произведение цифр = '))
result = False

for i in range(a):
    if result:
        break
    for j in range(b):
        if (i + j == a) and (i*j == b):
            print(i,j)
            result = True
            break
