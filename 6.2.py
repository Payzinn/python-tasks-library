def first():
    def histogramm(string):
        sym_dict = dict()
        for i in string:
            if i in sym_dict:
                sym_dict[i] += 1
            else:
                sym_dict[i] = 1

        return sym_dict

    text = input('Введите текст: ').lower()
    hist = histogramm(text)
    
    for i_sym in sorted(hist.keys()):
        print(i_sym, ":", hist[i_sym])
    print('Максимальная частота: ', max(hist.values()))

def second():

    phonebook = {
        'Ваня': 100,
        "Петя": 200,
        "Алиса":300
    }

    other = {
        "Игорь": 1000,
        "Петя": 800,
        "Алена": 2000
    }

    phonebook.update(other)
    phonebook["Гоша"] = phonebook.pop('Игорь') 

    for i in phonebook:
        print(i, phonebook[i])

    print(phonebook.get("Степан"))

#home task

def one():
    small_storage = {

    'гвозди': 5000,

    'шурупы': 3040,

    'саморезы': 2000

}

    big_storage = {

        'доски': 1000,

        'балки': 150,

        'рейки': 600

}
    
    big_storage.update(small_storage)
    product = input('Введите название товара: ')
    if big_storage.get(product) == None:
        print("Товара нет.")
    else:
        print(product,big_storage[product])

def two():
    incomes = {
        'apple': 5600.20,
        'orange': 3500.45,
        'banana': 5000.00,
        'bergamot': 3700.56,
        'durian': 5987.23,
        'grapefruit': 300.40,
        'peach': 10000.50,
        'pear': 1020.00,
        'persimmon': 310.00,
    }


    def get_value(x):
        return x[1]


    result_sum = sum(incomes.values())
    min_name, min_value = min(incomes.items(), key=get_value)
    # При помощи функции и параметра key мы говорим пайтону как именно надо сравнивать между собой элементы
    # Т.к. элементы записаны в таком виде - ('apple': 5600.20), а сравнивать мы хотим по значениям - то нам проосто надо брать для сравнения
    # элементы под индексом 1 (если бы сравнивали по ключам, то индекс надо было бы заменить на 0)
    print(result_sum, min_name, min_value)

def three():
    def counter(string):
        alphabet = dict()
        for i in string:
            if i in alphabet:
                alphabet[i] += 1
            else:
                alphabet[i] = 1

        return alphabet
    
    text = input('Введите текст: ').lower()
    result = counter(text)
    for i in sorted(result.keys()):
        print(f'{i} : {result[i]}')
    print(f'Максимальная частота {max(result.values())}')

three()