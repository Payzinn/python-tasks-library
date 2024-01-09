def divide(number):
    return 10 / number

def sum_of_divide(left, right):
    div_sum = 0

    for digit in range(left, right + 1):
        try:
            div_sum += divide(digit)
            print(div_sum)
        except ZeroDivisionError:
            print('На 0 делить нельзя!')

    return div_sum

total = 0

try:
    numbers_file = open('digits.txt', 'r')

    for i_line in numbers_file:
        nums_list = i_line.split()
        first_num = int(nums_list[0])
        second_num = int(nums_list[1])
        
        total += sum_of_divide(first_num, second_num)
        print('Общая сумма {}'.format(total))

except ValueError:
    print('Данные нельзя преобразовать в целое число')
except FileNotFoundError:
    print('Не удаётся найти указанный файл, проверьте путь')

answer_file = open('answer.txt', 'w')
try:
    answer_file.write('The answer is: ')
    answer_file.write(str(total))
except TypeError as exc:
    print('\n',type(exc),' - Ошибка записи в файл, тип данных не строка')

else:
    print('Программа выполнилась без ошибок')

finally:
    answer_file.close()
    print(answer_file.closed)