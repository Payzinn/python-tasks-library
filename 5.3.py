def first():
    text = input('Содержимое файла: ')
    words_list = text.split()
    print(words_list)

    new_text = '---'.join(words_list)
    print(new_text)


def second():
    while True:
        grats_template = input('Введите шаблон поздравления, в шаблоне нужно использовать конструкцию {name} и {age}: ')

        if "{name}" in grats_template and "{age}" in grats_template:
            break
        print('Ошибка отсутствует конструкция {name} и/или {age}')

    names_list = input('Список людей через запятую: ').split(', ')
    age = input('Возраст людей через пробел: ')
    ages = [int(i) for i in age.split()]

    for i_man in range(len(names_list)):
        print(grats_template.format(name = names_list[i_man], age = ages[i_man]))

    people = [' '.join([names_list[i_man], str(ages[i_man])]) for i_man in range(len(names_list))]
    people_str = ', '.join(people)
    print(f'\nИменники: {people_str}')

#home task

def one():
    three_words = input('Введите три слова через пробел: ').split()
    counter = 0
    text = input('Введите текст:')
    for word in three_words:
        if word.lower() in text.lower():
            counter += 1
    print(f'Слова пользователя встречаются: {counter} раза')


def two():
    text = input('Введите текст: ').split()
    new_text = ' '.join(text) 
    print(new_text)

