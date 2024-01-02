import os

def find_file(cur_path, file_name):
    
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('   Смотрим', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('Это директория')
            result = find_file(path, file_name)
            if result:
                break
    
    else:
        result = None

    return result

file_path = find_file(os.path.abspath(os.path.join('..','python-tasks-library')), 'projects.py')

if file_path:
    print('Абсолютный путь к файлу: {}'.format(file_path))

else:
    print('Файл не найден')