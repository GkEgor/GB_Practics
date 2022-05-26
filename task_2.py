import os
my_project = {}

with open('config.yaml') as f:
    some_dict = dict(map(str.split, f.readlines()))

main_dir = some_dict.pop('main_dir')
for k, v in some_dict.items():
    os.makedirs(os.path.join(os.curdir, main_dir, k))
    for i in v.split(','):
       some_file = open(os.path.join(os.curdir, main_dir, k , i), 'w')
       some_file.close()


