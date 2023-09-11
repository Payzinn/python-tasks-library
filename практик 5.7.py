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

fourth()