def sym_change():

    word = input('Введите слово: ')
    replace_num=int(input('Номер символа для замены: '))
    replace_sym=input('Заменяем: ')

    sym_list=list(word)

    sym_list[replace_num-1] = replace_sym

    for i in sym_list:
        print(i, end='')

    print(f'\n{sym_list}')


def words_counter():

    words_list = []
    counts = [0, 0, 0]

    for i in range(3):
        word = input(f'Введите {i+1} слово: ')
        words_list.append(word)
    
    text = input("Слово из текста: ")

    while text != 'end':
        for index in range(3):
            if words_list[index] == text:
                counts[index] +=1

        text = input("Слово из текста: ")

    print('\n  Подсчёт слов в текста')
    
    for i in range(3):
        print(f'{words_list[i]} : {counts[i]}')

#words_counter()


def text_editor():

    text = input('Введите строку: ')
    a = len(text)
    words_list = list(text)
    replace_sym = ';'
    counter = 0

    for i in range(a):
        if words_list[i] == ':':
            words_list[i] = replace_sym
            counter +=1

    print('Исправленная строка: ',end='')

    for i in words_list:
        print(i,end='')

    print(f'\nКол-во замен {counter}')

# text_editor()

def neighbours():
    
    text=input('Введите строку: ')
    num=int(input('Номер символа: '))-1
    words_list=list(text)
    count=0
    print(f'Вот символ: {words_list[num]}')

    print(f'Символ слева {words_list[num-1]}\nСимвол справа {words_list[num+1]}')
    for index, letter in enumerate(words_list):
        if words_list[num] == words_list[index]:
            count+=1

    if count>0:
        print(f'Есть ещё {count-1} таких же символов')
    else:
        print('Таких же символов нет')
    
#neighbours()

