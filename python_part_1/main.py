def sqd(b):
    for num in b:
        print(f'{num} ** 2 = {num**2}')
def programm():
    b=[1,2,5,6,-7]
    print(f"вот список чисел: {b}")
    ask=input('Добавить число(y/n): ')
    if ask=='y':
        amount=int(input('Сколько чисел добавить: '))
        for _ in range (amount):
            a = int(input('Введите число: '))
            b.append(a)
        print(f"вот обновлённый список чисел: {b}")
    else:
        print('\n Похуй\n')

    ask_second=int(input('Что вы хотите сделать? \n1)Возвести в квадрат все числа\n2)Ещё что-то\n'))
    if ask_second==1:
        sqd(b)
    else:
        print('Пока')
        exit
def game():
    scores = [8, 5, 10, 7, 6]
    print(f'Список: {scores}')
    scores[1]*=3
    print(f'Список новый: {scores}')

game()