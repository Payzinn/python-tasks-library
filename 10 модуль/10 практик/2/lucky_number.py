import random

number_sum = 0
with open('outfile.txt', 'w') as numbers_file:
    while True:
        number_input=int(input('Введите число: '))
        try:
            if random.randint(1,13) == 1:
                print(random.randint(1,700))
                raise Exception('Вас постигла неудача!')
                
            
        except Exception as exc:
            print(exc)
            break

        numbers_file.write(str(number_input) + '\n')
        number_sum += number_input

        if number_sum >= 777:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
            break


        
