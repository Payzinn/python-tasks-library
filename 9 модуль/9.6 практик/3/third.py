import os
path = input('Путь: ')
dir_count = 0
file_count = 0
size_kb = 0

for i_elem in os.listdir(path):
    if os.path.isdir(i_elem):
        dir_count += 1
    
    elif os.path.isfile(i_elem):
        file_count += 1
        size_kb = os.path.getsize(i_elem)

result = round(size_kb / 1024,3)

print('Кол-во каталогов: {}\nКол-во файлов: {}\nРазмер в КБ: {}Kb '.format(dir_count,
                                                                         file_count,
                                                                         result))