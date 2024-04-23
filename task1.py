
from logger import input_data, print_data, edit_data, delete_data, find_contact

def interface():
    print('Добрый день! вы попали в телефонный справочник!\n1-Запись контакта\n2-Список контактов\n3-Внести изменения\n4-Удалить контакт\n5-Поиск контакта')
    command = int(input("Выберите команду: "))
    
    while command<1 and command >5:
        print("Неправильный ввод")
        command= int(input("Выберите команду: "))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        delete_data()
    elif command == 5:
        find_contact()