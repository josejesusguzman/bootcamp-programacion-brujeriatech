from itertools import groupby
for key, grupo in groupby(input()):
    print('({}, {})'.format(len(list(grupo)), key), end=" ")
