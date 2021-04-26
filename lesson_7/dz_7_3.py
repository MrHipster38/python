import os
import shutil

root_folder = 'my_project'
for root, dirs, files in os.walk(root_folder):
    print(root, dirs, files)
    for file in files:
        if file.endswith('.html'):
            dir_path = os.path.join(root_folder, 'templates', root.split('\\')[-1])
            try:
                os.makedirs(dir_path)
            except FileExistsError:
                pass
            shutil.copy(os.path.join(root, file), dir_path)
