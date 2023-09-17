def first():
    phonebook_dict = {
        'Ваня': 8800535666,
        'Колян': 92351255,
        'Вика': 86667771337
    }

    name = input('Введите имя: ')
    if name in phonebook_dict:
        print(phonebook_dict[name])
    else:
        print('Ошибка, человек с именем {} не найден '.format(name))

def second():
    student_str = input('Введите информацию о студенте через пробел\n(имя, фамилия, город, место учёбы, оценки)')
    student_info = student_str.split()
    student = dict()
    student['Имя'] = student_info[0]
    student['Фамилия'] = student_info[1]
    student['Город'] = student_info[2]
    student['Место учёбы'] = student_info[3]
    student['Оценки'] = []
    for i in student_info[4:]:
        student['Оценки'].append(int(i))
    
    for m in student:
        print(f'{m} - {student[m]}')

    
#HomeTask

def one():
    num = int(input("Введите целое число: "))
    result = dict()
    for i in range(1, num+1):
        result[i] = i**2
    print(result)



def two():
    current_contacts = {}
    while True:
        print("Текущие контакты на телефоне:")
        if current_contacts:
            for name in current_contacts:
                print(name, current_contacts[name])
        else:
            print("<Пусто>")
        new_contact = input("Введите имя: ")
        new_telephone = int(input("Введите номер телефона: "))
        if new_contact in current_contacts:
            print("Ошибка: такое имя уже существует.")
        else:
            current_contacts[new_contact] = new_telephone

