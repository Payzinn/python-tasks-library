names_list = []

while True:
    try:
        name_input = input('Введите имя: ')

        if name_input.lower() == 'error':
            raise BaseException('Ты сломал программу')

        if not name_input.isalpha():
            raise TypeError
        names_list.append(name_input)

        if len(names_list) == 5:
            print('Место закончилось')
            break

    except TypeError:
        print('Имя должно состоять только из букв')
    except BaseException:
        names_list = []
        print('Введено стоп слово')
        raise ValueError('Пожалуйста не вводите стоп слово')
    
names_file = open('names.txt', 'w', encoding='utf-8')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа выполнилась.')