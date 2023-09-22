def first():
    #Множества
    import random
    numbers_list = [random.randint(1,100) for _  in range(10)]

    unique = set(numbers_list)
    print(unique)

def second():
    nums_1 = {1,2,3,4,5}
    nums_2 = {4,5,6,7,8}
    #пересечение
    print(nums_1.intersection(nums_2))
    print(nums_1 & nums_2)
    #объединение
    print(nums_1.union(nums_2))
    print(nums_1 | nums_2)
    #разность
    print(nums_1.difference(nums_2))
    print(nums_1 - nums_2)

    nums_2.add(10)
    print(nums_2)
    nums_2.discard(4)
    print(nums_2)


#hometask

def one():
    user_input = set(input("Введите строку: "))
    symbols = set(".,;:!?")
    print("Количество знаков пунктуации:", len(user_input.intersection(symbols)))

def two():
    import random
    nums_1 = [random.randint(1,30) for _ in range(30)]
    nums_2 = [random.randint(1,30) for _ in range(30)]
    mn1 = set(nums_1)
    mn2 = set(nums_2)
    print('1-е множество: {}'.format(mn1))
    print('2-е множество: {}'.format(mn2))

    x = min(mn1)
    y = min(mn2)
    print('Минимальный элемент 1-го множества: {}'.format(x))
    print('Минимальный элемент 2-го множества: {}'.format(y))
    mn1.discard(x)
    mn2.discard(y)
    
    rand1 = (random.randint(100,200))
    rand2 = (random.randint(100,200))
    mn1.add(rand1)
    mn2.add(rand2)
    print('Случайное число для 1-го множества: {}'.format(rand1))
    print('Случайное число для 2-го множества: {}'.format(rand2))

    print('Объединение множеств: ', mn1 | mn2)
    print('Пересечение множеств:', mn1 & mn2)
    print('Элементы, входящие в nums_2, но не входящие в nums_1:', mn2 - mn1)
        


def three():
    text = input("Введите строку: ")
    text_set = set(text)
    digits_set = set()

    for i in text_set:
        if i.isdigit():
            digits_set.add(i)
    
    print('Различные цифры в строке: {}'.format(digits_set))

three()