file = open("text_2.txt", "r")
print(file.read(1))  # считываем 1 байт  H
print(file.tell())  # 1
file.seek(6)  # переставляет курсор на эту позицию
print(file.read())
