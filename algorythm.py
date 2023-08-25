from interface import *
from write_file import *

while True:
    interface()
    command = int(input('Введите команду: '))
    if command==1:
        person = input("Введите данные пользователя ")
        add_person(person)
    elif command==2:
        show_all()
    elif command==3:
        name = input("Введите элемент для поиска: ")
        search_element(name)
    elif command==4:
        name = input("Введите элемент для поиска: ")
        change_element(name)
    elif command==5:
        name = input("Введите элемент для поиска: ")
        delete_element(name)
    elif command == 6:
        break
    else:
        print("Ввод некорректен")