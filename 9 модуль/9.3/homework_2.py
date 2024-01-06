import os
import random

def find_file(cur_path, file_name):
    all_paths = []

    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)

        if file_name == elem:
            all_paths.append(os.path.abspath(path))
        
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            
            if result:
                all_paths.extend(result)
    
    return all_paths

def choose(file_name):
    file = open(file_name, 'r', encoding='utf-8')

    for line in file:
        print(line, end='')

    file.close()

all_paths = find_file('..','homework_1.py')
choose(random.choice(all_paths))