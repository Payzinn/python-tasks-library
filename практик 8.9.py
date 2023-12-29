def increment(start = 5, end = 100):
    if start <= end:
        print(start, end = ' ')
        increment(start + 1, end)

def second():
    site = {
    'html': {
        'head': {
        'title': 'Мой сайт'
},
            'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
}
}
}
    
    def find_key(struct, key, depth = None, current_depth = 0):
        if key in struct:
            return struct[key]
        
        if depth is not None and current_depth >= depth:
            return None

        for sub_struct in struct.values():
            print(sub_struct)
            print(current_depth)
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth, current_depth + 1)
                if result:
                    break
        else:
            result = None
            
        return result
        

    user_key = input('Какой ключ ищем: ')
    deep_ask = input('Хотите ввести максимальную глубину(y/n): ').lower()
    if deep_ask == 'y':
        depth = int(input('Введите максимальную глубину: '))
    value = find_key(site, user_key, depth)
    if value:
        print(value)
    else:
        print('Такого ключа нет')


def third():
    import copy

    def site_creator(site):
        count_ask = int(input('Сколько сайтов: '))
        for i in range(count_ask):
            new_site = copy.deepcopy(site)
            product = input('Введите название продукта для нового сайта: ')
            new_site["html"]["head"]["title"]= ("Куплю/продам {} недорого".format(product))
            new_site["html"]["body"]['h2']= ("У нас самая низкая цена на {}".format(product))
            print(new_site)


    site = {
'html': {
'head': {
'title': 'Куплю/продам {product} недорого'
},
'body': {
'h2': 'У нас самая низкая цена на {product}',
'div': 'Купить',
'p': 'Продать'
}
}
}
    site_creator(site)
     

def fourth():
    def summa(*args):
        def recursive_sum(item):
            if isinstance(item, int):
                return item
            elif isinstance(item, (list, tuple)):
                return sum(recursive_sum(i) for i in item)
            return 0
        
        total_sum = recursive_sum(args)
        print(total_sum)
    nums = [[[1], [5], (3)]]
    summa(nums)  
fourth()

# Сначала проверяется, является ли элемент [1], [2], (3) целым числом. Нет, это список/кортеж, поэтому переходим к следующему условию.

# Затем выполняется условие isinstance(item, (list, tuple)), которое проверяет, является ли элемент списком или кортежем. Да, это список/кортеж.

# Далее происходит рекурсивный вызов recursive_sum(i). При первой итерации i будет [1]. Функция recursive_sum([1]) вызывается во внутреннем sum().

# recursive_sum([1]) снова проверяет, является ли элемент [1] целым числом. Нет, это список.

# Затем снова выполняется условие isinstance(item, (list, tuple)), потому что [1] также является списком.

# Далее происходит следующая итерация рекурсивного вызова recursive_sum(i), где i теперь будет 1. Функция recursive_sum(1) вызывается внутри recursive_sum([1]).

# Теперь recursive_sum определяет, что 1 является целым числом, а не списком или кортежем, и возвращает 1.

# Внешняя итерация recursive_sum([1]) принимает 1 внутри sum().

# Теперь рассмотрим следующий элемент списка/кортежа [2] и повторим процесс. Функция recursive_sum([2]) вернёт 2.

# Наконец, для последнего элемента (3), recursive_sum(3) вернёт 3.

# Затем функция sum складывает все эти значения 1, 2 и 3, возвращая 1 + 2 + 3 = 6.

# Это значение 6 присваивается переменной total_sum.

# Вызов print(total_sum) выводит 6.

def five():
    new_list = []
    def open_list(item):
        if isinstance(item, int):
            new_list.append(item)
        elif isinstance(item, list):
            for i in item:
                open_list(i)

    nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
    open_list(nice_list)

    print(new_list)

#def sixth():



