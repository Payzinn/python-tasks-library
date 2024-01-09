import random
names = ['A', 'B','C','D','E','F','G','H','K','L']
try:
    file_ages = open('ages.txt', 'r')
    content = file_ages.read().split('\n')
    file_ages.close()
    result_file = open('result.txt', 'x')

    for i_line in content:
        result_file.write(random.choice(names) + ':' + i_line + '\n')
            
    result_file.close()

except (FileExistsError, PermissionError) as exc:
    print(type(exc),' Попытка создания файла, который уже существует.')
except IsADirectoryError as exc:
    print(type(exc),' Ожидался файл, но оказалась директория.')
except (TypeError, ValueError) as exc:
    print(type(exc),' Операция применена к несоответствующему объекту.')
except FileNotFoundError as exc:
    print(type(exc),' Файл не существует.')
