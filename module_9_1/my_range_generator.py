def my_range(x, y):

    while x < y:
        yield x
        x += 1


for i in my_range(0, 10):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9

print("\n")


a = (i for i in [1, 2, 3])  # хранит генератор, который выдаёт по 1 элементу
b = [x for x in [1, 2, 3]]  # хранит в себе уже все элемнеты
print(a)  # <generator object <genexpr> at 0x0000027483861E70>
print(b)  # [1, 2, 3]
