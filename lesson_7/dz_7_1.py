
import os
root_folder = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']
try:
    os.mkdir(root_folder)
    os.chdir(root_folder)
    for folder in folders:
        os.mkdir(folder)
except FileExistsError:
    print('Ахтунг! Данные папки уже существуют')

