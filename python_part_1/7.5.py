def first():
    phonebook_dict = {
        ('Петров','Ваня'): 88006663636,
        ('Егоров','Ваня'): 88006663333,
        ('Ульянов','Петя'): 88006664444,
        ('Сидорова','Лена'): 8800665555
    }
    phonebook_dict[('Сидорова','Алена')] = 109090
    for i_person in phonebook_dict:
        if 'Сидорова' in i_person:
            print(i_person[1], phonebook_dict[i_person])
    #print(phonebook_dict)

#home task

def one():
    def person(dictionary,series, number):
        for i in dictionary:
            if series in i and number in i:
                print(dictionary[i])
            else:
                print('Ошибка в серии или номере')
                break


    data = {

    (5000, 123456): ('Иванов', 'Василий'),

    (6000, 111111): ('Иванов', 'Петр'),

    (7000, 222222): ('Медведев', 'Алексей'),

    (8000, 333333): ('Алексеев', 'Георгий'),

    (9000, 444444): ('Георгиева', 'Мария')

}
    while True:
        serial = int(input('Введите серию: '))
        number = int(input('Введите номер: '))
        person(data,serial,number)


def two():
    contacts = {}
    surname = input('Введите фамилию (для выхода введите "q"): ')
    name = input('Введите имя (для выхода введите "q"): ')

    while surname.lower() != 'q' or name.lower() != 'q':
        if surname.lower() == 'q' or name.lower() == 'q':
            break  # Выход из цикла, если хотя бы один из вводов равен 'q'

        name_and_surname = (surname, name)

        if name_and_surname not in contacts:
            contacts[name_and_surname] = int(input("Введите номер телефона: "))
        else:
            print('Уже есть')

        print(contacts)

        surname = input('Введите фамилию (для выхода введите "q"): ')
        name = input('Введите имя (для выхода введите "q"): ')
        
two()