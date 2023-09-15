def first():
    available_menu = input('Доступное меню: ').split(';')
    now_menu = ', '.join(available_menu)
    print('Сейчас в меню есть: {}'.format(now_menu))

def second():
    text = input('Введите строку: ').split()
    text_list = []

    for i in text:
        text_list.append(len(i))
    
    word = text_list.index(max(text_list))
    print(f'Самое длинное слово: {text[word]}\nДлина этого слова: {max(text_list)} символов')

def third():
    special_symbols = '@, №, $, %, ^, &, *, ()'.split(',')
    extensions = '.txt, .docx'.split(',')
    file_name = input('Название файла: ')
    success = True
    for i in special_symbols:
        if file_name.startswith(i):
            print('Ошибка символа')
            success = False
            break
    for m in extensions:
        if file_name.endswith(m):
            success = True
            break
    else:
        print('Ошибка расширения')
        success = False

    if success:
        print('валид')
    else:
        print('невалид')

def fourth():
    text = input('Введите строку: ').title()
    print('Результат: {}' .format(text))



def fivth():
    digits = '0123456789'
    letters = 'Q W E R T Y U I O P A S D F G H J K L Z X C V B N M'
    success = False
    
    while success == False:
        digit_counter = 0
        pass_counter = 0
        letter_counter = 0
        password = input('Введите пароль: ')
        for i in password:
            if i in digits:
                digit_counter += 1

        if digit_counter < 3:
            print('цифр менее 3')
        else:
            pass_counter += 1 


        if len(password) < 8:
            print('длина менее 8')
        elif len(password) > 8 or len(password) == 8:
            pass_counter += 1

        for m in password:
            if m in letters:
                letter_counter += 1

        if letter_counter < 1:
            print('нет заглавной буквы')
        else:
            pass_counter +=1

        if pass_counter == 3:
            print('Это надёжный пароль')
            success = True
fivth()