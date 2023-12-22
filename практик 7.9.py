def first():
    students = {
    1: {
    'name': 'Bob',
    'surname': 'Vazovski',
    'age': 23,
    'interests': ['biology, swimming']
    },
    2: {
    'name': 'Rob',
    'surname': 'Stepanov',
    'age': 24,
    'interests': ['math', 'computer games', 'running']
    },
    3: {
    'name': 'Alexander',
    'surname': 'Krug',
    'age': 22,
    'interests': ['languages', 'health food']
    }
    }

    def interest_and_surname(students):
        interest_list = []
        counter = 0
        for i_interest in students:
            interest_list.extend(students[i_interest]['interests'])
            counter += len(students[i_interest]['surname'])
        return interest_list, counter

    id_and_age = []
    for i_age in students:
        id_and_age.append((i_age, students[i_age]['age']))

    main_function = interest_and_surname(students)
    print(main_function)
    print(id_and_age)

def second():
    def crypto(my_list):
        def isPrime(number):
            if number < 2:
                return False
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    return False
            return True
        new_list = []
        for index, item in enumerate (my_list):
            if isPrime(index):
                new_list.append(item)

        return new_list

    print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(crypto('О Дивный Новый мир!'))


def third():
    players = {
("Ivan", "Volkin"): (10, 5, 13),
("Bob", "Robbin"): (7, 5, 14),
("Rob", "Bobbin"): (12, 8, 2)
}
    
    new_list = []

    for (first_name, last_name), scores in players.items():
        new_list.append((first_name, last_name, *scores))
    print(new_list)

def fourth():
    import random
    original_list = [random.randint(0,10) for _ in range(11)]
    new_list = []
    time_list = []
    for item in original_list:
        time_list.append(item)
        if len(time_list) == 2:
            new_list.append(tuple(time_list))
            time_list = []
        
    print(new_list)

def five():
    def tpl_sort(tup):
        cont_float = any(isinstance(i, float) for i in tup)

        if cont_float:
            return tup
        else:
            return tuple(sorted(tup))

    # tpl = (6, 3, -1, 8, 4, 10, -5)
    # print(tpl_sort(tpl))


def sixth():
    contacts = {}

    while True:
        print(contacts)
        action = int(input('1.Добавить контакт. \n2.Найти человека.:'))
        if action == 1:
            name_and_surname = input('Введите фамилию и имя через пробел: ').split()
            name_and_surname = tuple(name_and_surname)
            if name_and_surname not in contacts:
                contacts[name_and_surname] = int(input("Введите номер телефона: "))
            else:
                print('Уже есть такой контакт')

        if action == 2:
            search_surname = input('Введите фамилию для поиска: ').lower()
            for i in contacts:
                if search_surname in i[1].lower():
                    print("\nРезультат поиска: ",i,contacts[i])
                


def seventh():
    def shortest(string, tpl):
        return min(len(string), len(tpl))

    text = "abc"
    numbers = (10, 20, 30, 40)

    pairs = ((text[i], numbers[i]) for i in range(shortest(text, numbers)))
    for i in pairs:
        print(i,end = '')


seventh()