user = input('Введите: ')
print(list(filter(lambda elem: not(elem.isupper() or elem.isdigit()), user)))