def first():
    my_list = ['Игра', 'Изгой', "Таксист"]
    your_list = ["Начало", "Отступники", "Король лев"]

    my_list.extend(your_list)

    print(my_list)

def second():

    pack = []
    decode = []
    bad_packs = 0

    packs = int(input("Колво пакетов: "))
    for i in range(packs):
        print(f"\nПакет номер {i+1}")
        for i_bit in range(4):
            print(f'{i_bit+1} бит: ', end=' ')
            num=int(input())
            pack.append(num)
            
        if pack.count(-1) <= 1:
            decode.extend(pack)
        else:
            print('Много ошибок в пакете')
            bad_packs += 1
        pack = []
    
    print(f'Полученное сообщение {decode}')
    print(f'Колво ошибок в сообщении: {decode.count(-1)}')
    print(f'Колво потерянных пакетов {bad_packs}')


#HomeTask

def cmps():

    main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

    first_company = [0, 0, 0]

    second_company = [1, 0, 0, 1, 1]

    third_company = [1, 1, 1, 0, 1]

    main.extend(first_company)
    main.extend(second_company)
    main.extend(third_company)

    print(f'Общий список задач {main}')
    print(f"Колво невыполненных задач: {main.count(0)}")

def virus():

    first_message = input("Первое сообщение: ")
    second_message = input("Второе сообщение: ")
    firstlen=len(first_message)
    seclen=len(second_message)
    if firstlen > seclen:
        print(f'Третье сообщение {first_message + second_message}')
    else:
        print(f'Третье сообщение {second_message + first_message}')
    
    if firstlen == seclen:
        print('Ой')

