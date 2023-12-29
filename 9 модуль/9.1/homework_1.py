import os
folder_name = 'access'
file_name = "admin.bat"
rel_path = os.path.join(file_name)
print(rel_path)

abs_path = os.path.abspath(os.path.join(folder_name, file_name))
print(abs_path)
