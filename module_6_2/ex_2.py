import os

# перемещаем файл в папку
os.rename("asd.txt", r"A\asd.txt")
# опять переименовываем файл
os.replace(r"A\asd.txt", r"A\text.txt")
