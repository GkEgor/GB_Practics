import os.path
some_dir = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in folders:
    os.makedirs(os.path.join(os.curdir, some_dir, folder), exist_ok=True)
