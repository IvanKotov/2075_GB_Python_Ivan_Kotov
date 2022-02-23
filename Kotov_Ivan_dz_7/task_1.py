from os import mkdir
from os.path import exists, join as path

base = 'my_project'
my_dir = ['settings', 'mainapp', 'adminapp', 'authapp']

if not exists(base):
    mkdir(base)


for i in my_dir:
    my_path = path(base, i)
    if not exists(my_path):
        open(my_path, 'a').close()
