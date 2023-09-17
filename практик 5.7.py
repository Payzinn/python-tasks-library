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


def sixth():
    s = input("Введите строку: ")

    count = 1
    result = ""

    for i in range(len(s)):
        if i > 0 and s[i-1] == s[i]:
            count += 1
        else:
            if i > 0:
                result += str(count)
            result += s[i]
            count = 1

    result += str(count)
    print("Закодированная строка: {}".format(result))

def seventh():
    while True:
        ip = input('Введите IP: ')
        parts = ip.split('.')

        if len(parts) != 4:
            print('Адрес — это четыре числа, разделённые точками.')
            continue

        valid_ip = True
        for part in parts:
            if not part.isdigit():
                print(f'{part} — это не целое число.')
                valid_ip = False
                break

            num = int(part)
            if num < 0 or num > 255:
                print(f'{num} превышает 255.' if num > 255 else f'{num} меньше 0.')
                valid_ip = False
                break

        if valid_ip:
            print('IP-адрес корректен.')
            break

def eight():
    first_string = input('Первая строка: ')
    second_string = input('Вторая строка: ')

    if len(first_string) > len(second_string):
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
        exit()
    
    if sorted(first_string) != sorted(second_string):
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
        exit()
    
    n = len(first_string)

    for i in range(n):
        s = second_string[i:] + second_string[:i]

        if s == first_string:
            print('Первая строка получается из второй со сдвигом {}'.format(i))
            exit()

    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")



def nine():
    def count_uppercase_lowercase(text):
        uppercase = 0
        lowercase = 0
        for i in text:
            if i.islower():
                lowercase += 1
            elif i.isupper():
                uppercase += 1
        return uppercase, lowercase

    text = input("Введите строку для анализа: ")
    uppercase, lowercase = count_uppercase_lowercase(text)
    print("Количество заглавных букв:", uppercase)
    print("Количество строчных букв:", lowercase)


nine()