file = open("text_4.txt", "w")


try:
    # есть вероятность,что ничего не запишется и файл не будет закрыт из-за поднятой ошибки
    file.write("afghdfh")

except TypeError:
    pass
finally:
    file.close()
