# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 5. Добавить контакт

# contact = 'Петр Петрович Терентьев 2345667890'
contacts_file = r'/Users/sergejveletnuk/Desktop/Pythone_HomeWork/contact_phone.txt'


def append_contact(contacts_file):
    contact = input('Введите контакт в формате Ф И О Телефон:')
    with open(contacts_file, 'a', encoding="utf-8") as f:
        f.write(f'\n{contact}')
    print ('Контакт добавлен')
 
    
def read_file(contacts_file):
    with open(contacts_file, 'r', encoding="utf-8") as f:
        print(f.read())

def search_contact(contacts_file):
    search_by = input("Введите информацию для поиска (фамилия, имя или отчество):")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                print(line)
        

def delete_user():
    f = open("contact_phone.txt","r")
    lines = f.read()
    print(lines)
    contact = input('Введите контакт который хотите удалить:-->')
    f = open("contact_phone.txt","r")
    lines = f.readlines()
    if contact != '':
        f = open("contact_phone.txt","w")
        for line in lines:
            if line.find(contact) == -1:
            # if line!= contact +"\n":
                f.write(line)
    print('контакт удален!')
        
    
       
            


def change_contact():
    with open ('contact_phone.txt', 'r') as f:
        old_data = f.read()
        print(old_data)
    new_data = old_data.replace(input('кого вы ищите '), input('введите на кого вы хотите заменить -->'))
    print('Готово!')
    with open ('contact_phone.txt', 'w') as f:
        f.write(new_data)
        print(new_data)
    print ('Добро пожаловать!',
        '\n1) Вывести весь справочник',
        '\n2) Добавить контакт',
        '\n3) Найти контакт',
        '\n4) Удалить контакт',
        '\n5) Заменить контакт')



def user_action():
    print ('Добро пожаловать!',
        '\n1) Вывести весь справочник',
        '\n2) Добавить контакт',
        '\n3) Найти контакт',
        '\n4) Удалить контакт',
        '\n5) Заменить контакт')
    while (input1:= int(input('Выберите действие со справочником (0 = выход):'))) != 0:
        if input1 == 1:
            read_file(contacts_file)
        elif input1 == 2:
            append_contact(contacts_file)
        elif input1 == 3:
            search_contact(contacts_file)
        elif input1 == 4:
            delete_user()
        elif input1 == 5:
            change_contact()
        else:
            print("Некорректный ввод")

user_action()


    
