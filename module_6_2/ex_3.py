import os

print(os.getcwd())  # C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_6_2

# ['A', 'C', 'ex_1.py', 'ex_2.py', 'ex_3.py', 'file.txt', 'name.txt']
print(os.listdir())


def walk(path, list):
    print(list)
    print(os.getcwd())
    os.chdir(path)
    list_dir = list(filter(os.path.isdir, os.listdir()))

    for el in list_dir:
        list_dir.remove(el)
        walk(fr"{path}\{el}", list_dir)


walk(r"C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_6_2", [])
# print(os.chdir('A'))  # None    указали относительный путь

# C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_6_2\A
print(os.getcwd())
