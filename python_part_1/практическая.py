def first():
    #1 задача

    number=int(input('Введите число: '))
    odd_number_list=[]

    for i in range(1,number+1,2):
        odd_number_list.append(i)

    print(f'Список нечётных чисел от одного до {number}: {odd_number_list}')

#first()

def second():
    #2 задача

    list_of_participants=["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    length=len(list_of_participants)

    for i in range (0,length,2):
        print(list_of_participants[i])

#second()

def third():
    #3 задача

    gpu_list=[3070, 2060, 3090, 3070, 3090]
    new_gpu_list=[]

    for index, number in enumerate(gpu_list):
        if number<max(gpu_list):
            new_gpu_list.append(number)
    
    print(f'\nСтарый список: {gpu_list}\nНовый список: {new_gpu_list}\n')

#third()

def fourth():
    #4 задача

    films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
    print(f'Список фильмов: {films}')
    favourite_films=[]
    amount_of_films=int(input('Сколько фильмов хотите добавить: '))

    for i in range(amount_of_films):
        print(f'Вот i: {i} ')
        ask_film=input('Введите название фильма: ')
        if ask_film in films:
            favourite_films.append(ask_film)
        else:
            print(f'Ошибка: фильма {ask_film} у нас нет :(')

    print(f'\nВот список ваших любимых фильмов: ',end='')

    for x in favourite_films:
        print(x, end=', ')


    #print('Ваш список любимых фильмов:',',' .join(favourite_films))

#fourth()

def fivth():
    #5 задача
    container_amount=int(input('Введите кол-во контейнеров: '))
    container_list=[]

    for i in range(container_amount):
        container_weight=int(input('Введите вес контейнера: '))
        if container_weight<200:
            container_list.append(container_weight)
        else:
            print('Ошибка! Вес контейнера не может быть больше 200')
            exit()
    
    new_container=int(input('Введите вес нового контейнера: '))

    index = 0
    while index < len(container_list) and container_list[index] >= new_container:
        index += 1

    print("Номер, который получит новый контейнер:", index + 1)

#fivth()

def sixth():
    shift=int(input('Сдвиг: '))

    old_list=[1, 2, 3, 4, 5]
    new_list=[]
    a=len(old_list)
    shift%=a
    new_list = old_list[-shift:] + old_list[:-shift]

    print(f'Изначальный список: {old_list}')
    print(f'\nСдвинутый список: {new_list}')

#sixth()

def seventh():
        
    word = input('Введите слово: ')

    word_list = list(word) 
    reverse_list = list(word) 
    reverse_list.reverse()

    if word_list == reverse_list:
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')

#seventh()

def eight():
    numbers = [1, 4, -3, 0, 10]
    n=len(numbers)
    print(f'Изначальный список: {numbers}')
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    print(f'Отсортированный список: {numbers}')

#eight()

def nine():
    numbers = [] 
    ask=int(input('Сколько чисел добавить: '))
    for i in range(0,ask):
        num = int(input("Введите число: "))
        numbers.append(num)
        index = len(numbers) - 1 
    while index >= 0:
        if numbers[index] % 2 == 0:  
            print(numbers[index])
        index -= 1  


nine()