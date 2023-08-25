def add_person(person):
    data = open('data.txt', 'a', encoding='utf-8')
    data.write(person)
    data.write('\n')
    data.close()

def show_all():
    data = open ('data.txt', 'r', encoding = 'utf-8')
    for line in data:
        print(line[:-1])
    data.close()

def search_element(name):
    with open ('data.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            if name in line.split():
                print(line)
                break
        else:
            print('Такого нет')

def change_element(name):
    with open('data.txt', 'r', encoding='utf-8') as data_r:
        lines = data_r.readlines()

    with open('data.txt', 'w', encoding='utf-8') as data_w:
        for line in lines:
            if name in line.split():
                print(f"Старые данные: {line}")
                new_data = input("Введите новые данные: ") + '\n'
                line = new_data
                data_w.write(line)
                print("Данные успешно изменены.")
            else:
                data_w.write(line)


def delete_element(name):
    with open('data.txt', 'r', encoding='utf-8') as data_r:
        lines = data_r.readlines()

    with open('data.txt', 'w', encoding='utf-8') as data_w:
        for line in lines:
            if name in line.split():
                print(f"Удален контакт: {line}")
                new_data = ""
                line = new_data
                data_w.write(line)
            else:
                data_w.write(line)