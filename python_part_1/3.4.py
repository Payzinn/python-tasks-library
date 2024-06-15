def first():
    n = int(input('number: '))
    members = list(range(1, n+1))
    print(members)

def altFirst():
    step = 1
    n = int(input('number: '))
    members = []
    for _ in range(n // 3):
        members.append(list(range(step,step + 3)))
        step += 3
    print(members)

def altsecfir():
    members = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for team in members:
        for man in team:
            print(man, end = ' ')
        print()


def second():
    word_list = [ ['', 0], ['', 0], ['', 0] ]

    for num in range(3):
        word = input(f'Введите {num+1} слово: ')
        word_list[num] [0] = word
        
    text = input('Слово из текста: ')
    while text != 'end':
        for index in range(3):
            if word_list[index] [0] == text:
                word_list[index][1] += 1
        text = input('Слово из текста: ')

    print(f'\nПодсчёт слов в тексте')
    for index in range(3):
        print(f'{word_list[index][0]}: {word_list[index][1]}')


#HomeTask

def olympic():
    s = 1
    n = int(input('Введите кол-во участников: '))
    a = int(input('Кол-во участников в команде: '))
    members = []
    for i in range(n // a):
        members.append(list(range(s, s + a)))
        s+=a
    print(f'\nСписок: {members}')

olympic()