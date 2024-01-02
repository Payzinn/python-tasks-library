import os

path = input('Путь: ')

if os.path.isdir(path):
    print('Это папка')

elif os.path.isfile(path):
    print('Это файл')
    size = os.path.getsize(path)
    print('Размер файла: {} байт'.format(size))

else:
    print('Указанного пути не существует')