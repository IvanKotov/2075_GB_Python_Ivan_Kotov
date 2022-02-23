from os import walk
from os.path import join as path, getsize

size_files = []
for root, dirs, files in walk('.'):
    if not files:
        continue
    size_files.extend(getsize(path(root, i)) for i in files)

max_len = len(list(str(max(size_files))))
key = [10 ** i for i in range(2, max_len + 1)]

result = {}
for i in size_files:
    for j in key:
        if i < j:
            result.update({j: result.get(j, 0) + 1})
            break

result = dict(sorted(result.items(), key=lambda x: x))

for max_size, count in result.items():
    print(result)