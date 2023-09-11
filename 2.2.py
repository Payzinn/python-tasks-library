def game_first():
    #игра где просто второму игроку добавляются очки
    scores = [8, 5, 10, 7, 6]
    print(f'Список: {scores}')
    scores[1]*=3
    print(f'Список новый: {scores}')

def game_second():
    #игра про монстров
    monsters_count=int(input('Кол-во монстров: '))
    mage_index=int(input('Номер мага в списке: '))
    monsters_damage = []

    #Добавляю в список числа урона монстров
    for monster in range(monsters_count):
        damage_amount=int(input(f'Введите урон {monster+1}-го монстра: '))
        monsters_damage.append(damage_amount)

    #Маг добавляет свой урон всем другим монстрам кроме тех, у которых урон 100
    for i_monster in range(monsters_count):
        if monsters_damage[i_monster]<100 and i_monster!= mage_index-1:
            monsters_damage[i_monster]+= monsters_damage[mage_index-1]

    print(f'Урон монстров: {monsters_damage}')

#game_second()

def max_digit():
    #Максимальное число и минимальное
    nums_list = []

    N = int(input('Кол-во чисел в списке: '))

    for _ in range(N):

        num = int(input('Очередное число: '))

        nums_list.append(num)

    

    maximum = nums_list[0]

    minimum = nums_list[0]

    for i in nums_list:

        if maximum < i:

            maximum = i

        if minimum > i:

            minimum = i

    

    print('Максимальное число в списке:', maximum)

    print('Минимальное число в списке:', minimum)

#max_digit()

def krat():
    num_count=int(input('Введите колво чисел в списке: '))
    numbers=[]
    summa=0

    for i in range(num_count):
        digit=int(input(f'Введите {i+1} число: '))
        numbers.append(digit)
        print(' ')
    
    divider=int(input('\nВведите делитель: '))

    for index, num in enumerate(numbers):
        if num % divider == 0:
            print(f'Индекс числа {num}: {index} ')
            summa+=index
    
    print(f'Сумма индексов {summa}')

#krat()


def dog_jog():

    #меняет местами наибольший и наименьший элементы в списке.

    dogs_list=[]

    dogs_count=int(input('Сколько собак учавствует в забеге: '))

    for i in range (dogs_count):
        dog_score=int(input(f'Введите кол-во очков {i+1} собаки: '))
        dogs_list.append(dog_score)

    if dogs_list:
        maximum = dogs_list[0]
        minimum = dogs_list[0]

        minimum_index = 0
        maximum_index = 0
        for index, i in enumerate(dogs_list):

            if maximum < i:
                maximum = i
                maximum_index = index

            if minimum > i:
                minimum = i
                minimum_index = index

        print('Максимальное число в списке:', maximum)
        print('Минимальное число в списке:', minimum)

        print(dogs_list)
        dogs_list[minimum_index], dogs_list[maximum_index] = dogs_list[maximum_index], dogs_list[minimum_index]
        print(dogs_list)

#dog_jog()




