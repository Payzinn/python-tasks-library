import os
folder_name = "project"
file_name = "my_project.txt"

path = ("docs/{folder}/{file}".format(
    folder = folder_name,
    file = file_name))

print(path)

rel_path = os.path.join('docs', folder_name, file_name)
print(rel_path)

abs_path = os.path.abspath(file_name)
print(abs_path)

print(os.path.abspath('../new_folder'))# не для всех систем
print(os.path.abspath(os.path.join('..', 'new_folder')))# подойдёт для любой системы
print(os.path.abspath('/root_of_drive'))# не для всех систем
print(os.path.abspath(os.path.join(os.path.sep, "for_every_os_root")))#подойдёт для всех систем