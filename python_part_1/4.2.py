def first():
    squares = [x**2 for x in range (10)]
    print(squares)

def second():
    def get_higher_price(percent, price):
        return round(price*(1 + percent / 100), 2)
    
    prices_now = [1.09, 23.56, 57.84, 4.56, 6.78 ]
    first_percent = int(input('Повышение на первый год: '))
    second_percent = int(input('Повышение на второй год: '))
    prices_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
    prices_second = [get_higher_price(second_percent, i_price) for i_price in prices_first]
    print(f'Сумма цен за каждый год: {round(sum(prices_now),2), round(sum(prices_first),2), round(sum(prices_second),2)}')

#HomeTask

def one():
    a = int(input('Левая граница: '))
    b = int(input('Правая граница: '))+1
    cubes = [x**3 for x in range(a,b)]
    squares = [x**2 for x in range (a,b)]
    print(f'Кубы: {cubes}')
    print(f'Квадраты: {squares}')

def two():
    string = input('Введите строку: ')
    element = input('Введите дополнительный элемент: ')
    double = [x*2 for x in string]
    special_elment = [x + element for x in double]
    print(f'Список удвоенных символов: {double}')
    print(f'Склейка с дополнительным символом: {special_elment}')

def three():
    def get_higher_price(percent, price):
        return round(price * (1 + percent/100),2)
    prices_now = []
    for i in range(5):
        price = float(input(f"Цена на товар {i+1}: "))
        prices_now.append(price)
    first_percent = int(input('Повышение на первый год: '))
    second_percent = int(input('Повышение на первый год: '))
    first_price = [get_higher_price(first_percent, i_price) for i_price in prices_now]
    second_price = [get_higher_price(second_percent, i_price) for i_price in first_price]
    print(f'Сумма цен за каждый год: {round(sum(prices_now),2), round(sum(first_price),2), round(sum(second_price),2)}')

