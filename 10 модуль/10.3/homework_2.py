import os
nums = []
result = 0
file_path = os.path.join('numbers.txt')
numbers_file = open(file_path, 'r', encoding='utf-8')
try:
    for line in numbers_file:
        nums.append(int(line))

    result = sum(nums)
except (ValueError, TypeError) as exc:
    print(type(exc), '- Данные нельзя преобразовать в целое число')

answer_file = open('answer_2.txt', 'w')

try:
    answer_file.write(str(result))
except TypeError as exc:
    print(type(exc), '- Ошибка записи в файл, тип данных не строка')

finally:
    answer_file.close()
    numbers_file.close()
    print(answer_file.closed)
    print(numbers_file.closed)
