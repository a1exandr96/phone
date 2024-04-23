import csv
from data_create import name_data, surname_data, phone_data, adress_data



def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
   
    with open('data_first.csv', "a", encoding="utf-8") as f:
        f.writelines(f"{name};{surname};{phone};{adress}\n")
   
   
def print_data():
    print('Вывожу список контактов: \n')
    with open('data_first.csv', 'r', encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_sp = []
        j = 0 
        for i in range(len(data_first)):
            if data_first[i]=="\n" or i == len(data_first) - 1:
                data_first_sp.append(''.join(data_first[j:i + 1]))
    
    print("".join(data_first_sp))
        


def edit_data():
    with open('data_first.csv', "r", encoding="utf-8") as file:
        data = file.read().split("\n")
   
    print("Это список контактов:")
    for i in range(len(data)):
        print(f"Контакт {i + 1}: {data[i]}\n")
    
    index = int(input("Введите номер контакта, который хотите изменить: ")) - 1
    
    new_data = input("Введите новые данные через запятую (name, surname, phone, adress): ").split(", ")
    data[index] = "\n".join(new_data)
    print("Контакт успешно изменен!")
    
    with open("data_first.csv", "w", encoding="utf-8") as file:
        file.write("\n".join(data))


def find_contact():
    search_query = input("Введите данные для поиска контакта: ")
    found_contacts = []
    with open('data_first.csv', 'r', encoding="utf-8") as f:
        for line in f:
            if search_query.lower() in line.lower():
                found_contacts.append(line)
    
    if found_contacts:
        print("Найденные контакты:")
        for contact in found_contacts:
            print(contact)
    else:
        print("Контакт не найден")

def delete_data():
    with open('data_first.csv', "r", encoding="utf-8") as file:
        data = file.readlines()
   
    print("Список контактов:")
    for i, contact in enumerate(data, 1):
        print(f"Контакт {i}: {contact}")
    
    index_to_delete = int(input("Введите номер контакта для удаления: ")) - 1
    
    if 0 <= index_to_delete < len(data):
        del data[index_to_delete]
        with open("data_first.csv", "w", encoding="utf-8") as file:
            file.writelines(data)
        print("Контакт успешно удален!")
    else:
        print("Некорректный номер контакта. Удаление не выполнено.")
