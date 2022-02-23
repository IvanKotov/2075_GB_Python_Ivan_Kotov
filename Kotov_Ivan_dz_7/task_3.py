from os import mkdir, sep, walk
from os.path import exists, join as path
from shutil import copy2



paths = {}
paths_dirs = []
my_dir = 'my_project'

for root, dirs, files in walk(my_dir):
    for i in files:
        if i.endswith('.html'):
            template = path(*root.split(sep)[-1:])
            if template not in paths:
                paths_dirs.append(path(my_dir, 'templates', template))

            html_path = path(root, i)
            paths.update({html_path: path(my_dir, 'templates', template, i)})

if not exists(path(my_dir, 'templates')):
    mkdir(path(my_dir, 'templates'))

for _ in paths_dirs:
    if not exists(_):
        mkdir(_)

for old, new in paths.items():
    if not exists(new):
        copy2(old, new)