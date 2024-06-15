import os

def withdraw_code(cur_path):
    has_file = False

    for element in os.listdir(cur_path):
        path = os.path.join(cur_path, element)
        zvezds = '*'*40

        if os.path.isfile(path):
            has_file = True
            
            file_to_read = open(path, 'r', encoding='utf-8')
            content = file_to_read.read()
            file_to_read.close()

            file_to_write = open('drugs_2.txt', 'a', encoding='utf-8')
            file_to_write.write(content + '\n{}\n'.format(zvezds))
            file_to_write.close()

        elif os.path.isdir(path):
            withdraw_code(path)

    if not has_file and os.listdir(cur_path) == []:
        print('Не найдено', cur_path)

path_to_file = withdraw_code(os.path.abspath(os.path.join('..', 'Desktop')))
# print(os.path.abspath(os.path.join(os.path.sep)))