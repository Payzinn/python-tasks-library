def first():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]
    a.extend(b)
    t = a.count(5)
    print(t)
    for i in a:
        if i == 5:
            a.remove(i)
    a.extend(c)
    t = a.count(3)
    print(t)
    print(a)
first()

def second():
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 5, 6, 8, 10]
    list1.extend(list2)
    list1.remove(5)
    list1=sorted(list1)
    print(list1)

def third():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    detail_name = input('Название детали: ')
    detail_amount = 0
    for item in shop:
        if item[0] == detail_name:
            detail_amount += 1
    print('кол-во деталей: {}'.format(detail_amount))
    price = 0

    for item in shop:
        if item[0] == detail_name:
            price += item[1]

    print('Общая стоимость: {}'.format(price))



def fourth():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    while True:
        print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
        ask = input('Гость пришёл или ушёл(1/2): ')

        if ask == '1':
            name = input('Имя гостя: ')
            if len(guests)==6:
                print(f'Прости, {name}, но мест больше нет')
            else:
                guests.append(name)
                print(f'Привет {name}')
        if ask == '2':
            name = input('Имя гостя: ')
            if name in guests:
                guests.remove(name)
                print(f'Пока {name}')
            else:
                print('Таких нет')


def five():
    duration = 0


    violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]]
    
    amount_songs = int(input('Сколько песен выбрать: '))
    for i in range(amount_songs):
        name_song = input(f'Название {i+1} песни: ')
        found = False
        for song in violator_songs:
            if name_song == song[0]:
                duration += song[1]
                found = True
                break
        if not found:
            print('Такой песни нет')

    print(f'\nОбщее звучание песен - {duration}')

def sixth():
    counter = 0
    roll_size = []
    foot_size = []
    roll_amount = int(input("Введите кол-во роликов: "))

    for i_roll in range(roll_amount):
        size = int(input(f"Размер пары {i_roll+1}: "))
        roll_size.append(size)

    people_amount = int(input("Количество людей: "))

    for _ in range(people_amount):
        feet_size = int(input("Размер ноги человека: "))
        foot_size.append(feet_size)

    for roll in roll_size:
        for man in foot_size:
            if roll == man:
                counter += 1
                foot_size.remove(man)  
                break  

    print(f"Наибольшее количество людей, которые могут взять ролики: {counter}")


def seventh():
    n = int(input("Количество человек: "))
    k = int(input("Какое число в считалке? "))
    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        print(f'\nТекущий круг людей {people}')
        index = index % len(people)
        print(f'Начало счёта с номера {people[index]}')
        index = (index + k - 1) % len(people)
        print(f'Выбыл человек под номером {people[index]}')
        people.remove(people[index])

    print("Остался человек под номером", people[0])


# def min_additions(seq):
#     n = len(seq)
#     rev_seq = seq[::-1]
#     dp = [[0]*(n+1) for _ in range(n+1)]
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if seq[i-1] == rev_seq[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#     lcs_len = dp[n][n]
#     num_additions = n - lcs_len
#     additions = rev_seq[lcs_len:]
#     return num_additions, additions

# seq = [1,2,3,4,5]
# num_additions, additions = min_additions(seq)
# print(f"Минимальное количество чисел, которые нужно добавить: {num_additions}")
# print(f"Числа, которые нужно добавить: {additions}")