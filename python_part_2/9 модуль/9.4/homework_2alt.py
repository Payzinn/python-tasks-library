import os

def find_file(cur_path, ending):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)

        if i_elem.endswith(ending):
            all_paths.append(os.path.abspath(path))

        elif os.path.isdir(path):
            result = find_file(path, ending)

            if result:
                all_paths.extend(result)

    return all_paths

def get_file_text(path_to_file):
    file = open(path_to_file, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content

all_paths = find_file('..', '.py')
file_result = open('scripts.txt', 'w', encoding='utf-8')

for file_path in all_paths:
    file_result.write(get_file_text(file_path))
    file_result.write('\n'*2+'*'*40+'\n'*2)