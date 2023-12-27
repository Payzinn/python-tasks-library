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
     

third()