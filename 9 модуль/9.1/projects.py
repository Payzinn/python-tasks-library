import os

def print_list_dir(project):
    print('\nСодержимое папки проекта', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('  ', path)


projects_list = ['Skillbox', 'MyProject']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join(i_project))
    print_list_dir(path_to_project)