nums_sum = 0
nums_count = 0

try:
    numbers_file = open('numbers.txt', 'r')

    for i_line in numbers_file:
        nums_count += 1
        nums_sum += int(i_line)

    numbers_file.close()
    print('Среднее арифметическое: ', round(nums_sum / nums_count,2))

except FileNotFoundError:
    print('Ошибка файл не найден\nили путь до файла указан не верно')
except ValueError:
    print('Нельзя преобразовать данные в целое число')