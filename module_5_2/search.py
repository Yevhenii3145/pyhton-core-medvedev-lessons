from re import search

result = search(r"^Hello", "Hello world")
print(result)  # <re.Match object; span=(0, 5), match='Hello'>
result = search(r"world$", "Hello world")
print(result)  # <re.Match object; span=(6, 11), match='world'>
result = search(r"^world$", "Hello world")
print(result)  # None
result = search(r"world", "Hello worlds")
print(result)  # <re.Match object; span=(6, 11), match='world'>
result = search(r"worlds", "Hello world")
print(result)  # None
result = search(r"worlds*", "Hello world")
print(result)  # result = search(r"worlds", "Hello world")
result = search(r"worlds*", "Hello worlds")
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
# тоесть здесь проверяется вхождение любого символа 0 или больше раз
result = search(r"worlds*", "Hello worldssssss")
print(result)  # <re.Match object; span=(6, 17), match='worldssssss'>
# 1 или больше вхождений
result = search(r"worlds+", "Hello world")
print(result)  # None
result = search(r"worlds+", "Hello worldsss")
print(result)  # <re.Match object; span=(6, 14), match='worldsss'>
result = search(r"worlds?", "Hello worldsss")  # 0 или 1 вхождение
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
result = search(r"worlds{3}", "Hello worldsss")  # 3 символов "s"
print(result)  # <re.Match object; span=(6, 14), match='worldsss'>
# 3 и больше символов "s"
result = search(r"worlds{3,}", "Hello worldsssssss")
print(result)  # <re.Match object; span=(6, 18), match='worldsssssss'>
# от 3 до 4 символов "s"
result = search(r"worlds{3,4}", "Hello worldsssssss")
print(result)  # <re.Match object; span=(6, 15), match='worldssss'>
# "ds" будет 0 или 1 раз
result = search(r"worl(ds)?", "Hello worldsss")
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
# 1 символ либо s либо e
result = search("world(s|e)", "Hello worlde")
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
# 1 символ либо s либо e
result = search("world[se]", "Hello worlds")
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
result = search("world\d", "Hello worlds")  # \d -поиск цифры
print(result)  # None
# \d* -0 и больше цифр
result = search("world\d*", "Hello world125")
print(result)  # <re.Match object; span=(6, 14), match='world125'>
# (\d|s)* - цифра или буква 0 или больше раз
result = search("world(\d|s)*", "Hello world12521223")
print(result)  # <re.Match object; span=(6, 19), match='world12521223'>
result = search("world(\d|s)*", "Hello worlds")
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
result = search("world(\w|s)*", "Hello worlds")
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
# \s -все пробельные символы
result = search("world(\s|s)*", "Hello world  ")
print(result)  # <re.Match object; span=(6, 13), match='world  '>
result = search("world.", "Hello worlds")
print(result)  # <re.Match object; span=(6, 12), match='worlds'>
result = search("world(\D|s)*", "Hello worldg1")  # \D - не число
print(result)  # <re.Match object; span=(6, 12), match='worldg'>
result = search("world[a-d]", "Hello worldb")
print(result)  # <re.Match object; span=(6, 12), match='worldb'>
result = search("world[a-d]", "Hello worlds")
print(result)  # None
# [a-dA-D0-3s] перечень из возможных символов
result = search("world[a-dA-D0-3s]", "Hello worldc")
print(result)  # <re.Match object; span=(6, 12), match='worldc'>
# после world должен быть любой cимвол кроме перечня [a-d]
result = search("world[^a-d]", "Hello worldg")
print(result)  # <re.Match object; span=(6, 12), match='worldg'>
