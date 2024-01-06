import os

def find_file(cur_path, file_name):
    print('переходим {}'.format(cur_path))

    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        print("  Смотрим", path)

        if file_name == elem:
            return path
        
        elif os.path.isdir(path):
            print('Это директория')
            result = find_file(path, file_name)
            
            if result:
                break
    
    else:
        return None
    
    return result

file_path = find_file(os.path.abspath(os.path.join('..', '..', '9 модуль')), 'search.py')
if file_path:
    print('Абсолютный путь {}'.format(file_path))
    file = open('search_history.txt', 'a', encoding='utf-8')
    file.write(file_path + '\n')
    file.close()

else:
    print('Путь не найден')