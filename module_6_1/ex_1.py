file = open("text.txt", "r")
print(file)  # <_io.TextIOWrapper name='text.txt' mode='r' encoding='cp1251'>
# считывает всё содержимое файла по умолчанию
text = file.read()
print(text)
file.seek(0)
while True:
    text = file.read(5)
    print(text)
    '''Hello
        worl
       d!
    '''
    if not text:
        break
file.seek(0)

# readline - считывает строку пока не встретит \n
print(file.readline())  # Hello world!
file.seek(0)
print(file.readlines())  # ['Hello world!\n']
file.close()

# file = open("text.txt", "w") перезаписывает файл
# file = open("text.txt", "x") записывает даные в файл, если файл существует - будет exception
# file = open("text.txt", "a") открываем файл на дозапись
# file = open("text.txt", "rb") чтение в бинарном режиме
