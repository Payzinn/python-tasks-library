def first():
    #path = "C:/{user}".format(user = user_name)
    user = input('Введите имя пользователя: ')
    file = input('Введите имя файла: ')

    path = (f'C:/{user}/docs/folder/{file}.txt')
    print(path)

def second():
    while True:
        grats_template = input('Введите шаблон поздравления, в шаблоне нужно использовать конструкцию {name}: ')

        if "{name}" in grats_template:
            break
        print('Ошибка отсутствует конструкция {name}')

    print('Введите список имён (заканчивается на end) ')
    names_list = []
    while True:
        name = input('Имя: ')
        if name != 'end':
            names_list.append(name)
        else:
            break

    for i_name in names_list:
        print(grats_template.format(name = i_name))


#home

def one():
    user_name = input('Имя: ')
    delivery_code = int(input('Номер заказа: '))
    message = 'Здравствуйте, {name}! Ваш номер заказа: {code}. Приятного дня!'.format(
        name = user_name, 
        code = delivery_code)
    print(message)


def two():
    name = input('Введите имя: ')
    amount = input('Введите долг: ')
    message = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!'.format(name, amount)
    print(message)

def three():

    ip_address = "{0}.{1}.{2}.{3}"
    numbers = []
    for _ in range(4):
        new_number = int(input("Введите число: "))
        if 0 <= new_number <= 255:
            numbers.append(new_number)

    print(ip_address.format(*numbers))

