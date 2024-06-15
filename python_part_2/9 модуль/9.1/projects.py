import os

def print_list_dir(project):
    print('\nСодержимое папки проекта', project)
    if os.path.exists(project):
        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)
            print('  ', path)
    else:
        print("Каталога проекта не существует,\nили его путь указан неверно")


projects_list = ['Prod','Skillbox', 'MyProject']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join(i_project))
    print_list_dir(path_to_project)