import os
folder =os.path.abspath(os.path.join('..','python-tasks-library'))

for i_elem in os.listdir(folder):
    print(folder, i_elem)