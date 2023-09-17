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
    student['Оценки'] = student_info[4]