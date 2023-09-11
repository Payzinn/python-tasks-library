def first():
    user = input('Введите имя пользователя: ')
    file = input('Введите имя файла: ')

    path = ('C:/{user}/docs/folder/{file}'.format(
        user = user,
        file = file
    ))
    if not path.endswith('.txt'):
        print('Ошибка неверное расширение файла')
    elif not path.startswith('C:/'):
        print('Неккоректный диск')
    else:
        print(f'Путь к файлу: {path}')


def second():
    word_list = []

    for i_num in range(3):
        print(f'Введите {i_num+1} слово: ', end=' ')
        word = input().lower()
        word_list.append(word)

    text = input('Введите текст: ').lower().split()

    print(f'\nПодсчёт слов в тексте')
    for i in range(3):
        print(word_list[i], ':', text.count(word_list[i]))



#home task

def one():
    
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    text = input('Введите сообщение: ').lower()
    step = int(input('Введите сдвиг: '))
    newlist = list(text)
    for i in newlist:
        if i == ' ':
            print(' ', end='')
            continue
        if i not in alphabet:
            continue
        x = alphabet.index(i)
        if x + step >= len(alphabet):
            x = x - len(alphabet)
        print(alphabet[x+step], end='')

def two():

    path = input('Путь к файлу: ')
    hdd = input('На каком диске лежит файл: ')
    extension = input('Требуемое расширение файла: ')
    if path.startswith(hdd) and path.endswith(extension):
        print('Путь корректен!')
    else:
        print('Путь некорректен')
        
def three():
    text = input("Введите текст: ")
    lowers = len([letter for letter in text if letter.islower()])
    uppers = len([letter for letter in text if letter.isupper()])

    if lowers > uppers:
        print("Результат:", text.lower())
    else:
        print("Результат:", text.upper())


three()