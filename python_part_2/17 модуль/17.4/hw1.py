from typing import List
while True:
    number = (input('Введите числа: '))
    print(sorted(list(map(lambda num: int(num), number.split()))))