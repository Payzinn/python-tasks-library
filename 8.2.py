def first():
    #n! = n * (n-1)
    def factorial(num): 
        if num == 1:
            return 1
        fact_n_minus_1 = factorial(num-1)
        return num * fact_n_minus_1
        
    num_fact = factorial(5)
    print(num_fact)


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

    def find_key(struct, key):
        if key in struct:
            return struct[key]
        
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key)
                if result:
                    break
        else:
            result = None
        
        return result

    user_key = input("Какой ключ ищем: ")
    value = find_key(site, user_key)
    if value:
        print(value)
    else:
        print('Такого ключа нет')

second()

#hometask

def one():
    def factorial(num):
        if num == 1:
            return 1
        return num * factorial(num - 1)
    num = 5
    result = factorial(num)
    print(result)
    
def two():
    def power(a, n):
        if n <= 0:
            return 1
        return a * power(a, n - 1)

    # float_num = float(input('Введите вещественное число: '))
    # int_num = int(input('Введите степень числа: '))
    counter = 1
    float_num = 5.5
    int_num = 5
    print(f"{float_num} ** {int_num} = {power(float_num, int_num)}")
    # power(2.5, 0) = 1
    # power(2.5, 1) = 2.5 * 1 = 2.5
    # power(2.5, 2) = 2.5 * 2.5 = 6.25
    # power(2.5, 3) = 2.5 * 6.25 = 15.625
    # power(2.5, 4) = 2.5 * 15.625 = 39.0625
    # power(2.5, 5) = 2.5 * 39.0625 = 97.65625

