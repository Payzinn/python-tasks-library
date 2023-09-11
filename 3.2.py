def first():
    langs=['Python', 'Java', 'JS', 'SQL']
    user=input('После чего вставить: ')
    i_lang = langs.index(user)
    langs.insert(i_lang+1, 'C++')
    print(langs)


def second():
    films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист', 

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня', 

    'Проклятый остров', 'Начало', 'Матрица'

]
    
    favourite_films=[]

    while True:
        print(f'\nВаш текущий топ фильмов {favourite_films}')
        new_movie = input('Название фильма: ')

        if new_movie in films:
            print('Команды: добавить (1), удалить(2), вставить(3)')
            command=int(input('Введите номер команды: '))

            if command == 1:
                favourite_films.append(new_movie)

            if command == 2:
                if new_movie in favourite_films:
                    favourite_films.remove(new_movie)
                else:
                    print('Этого фильма нет в вашем списке')

            if command == 3:
                index=int(input('На какое место: '))
                favourite_films.insert(index - 1, new_movie)
        else:
            print('Этого фильма не существует')

def third():

    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    print(f'Изначальный список: {zoo}')
    zoo.remove('elephant')
    print(f'Слон ушёл, новый список: {zoo}')
    zoo.insert(1, 'bear')
    print(f'Поселили медведя между львом и обезьяной: {zoo}')
    i_zoo= zoo.index("lion")
    i_zoom=zoo.index("monkey")
    print(f'Лев сидит в клетке номер {i_zoo+1}\nОбезьяна сидит в клетке номер {i_zoom+1}')
    


def fourth():

    employee_counter = 0
    employees = []
    employee_amount = int(input('Введите кол-во сотрудников: '))

    for i in range(employee_amount):
        salary=int(input(f'Зарплата сотрудника {i+1}: '))
        if salary > 0:
            employees.append(salary)
            employee_counter += 1

    # for m in range(0, employee_amount-1):
    #     if employees[m] == 0:
    #         employees.remove(employees[m])
    #         employee_counter -= 1

    print(f'\nОсталось сотрудников {employee_counter} \nЗарплаты {employees}\nМаксимальная ЗП {max(employees)}\nМинимальная ЗП {min(employees)}')

fourth()