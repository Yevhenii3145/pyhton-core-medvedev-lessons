# корттеж-неизменяемая, упорядоченная коллекция НЕ уникальных элементов
# print(help(tuple))
new_tuple = tuple([1, 2, 3])
print(new_tuple)
print(type(new_tuple))

print(new_tuple[1])  # 2
# new_tuple[1] = 77  TypeError: 'tuple' object does not support item assignment

# чтобы создать кортеж из одного элемента нужно добавить запятую
t = (1,)
print(type(t))  # <class 'tuple'>

a = 10
b = 20
c = a  # без ипользования свойств кортежей нужна промежуточная переменная
a = b
b = c
print(a)
print(b)

a = 10
b = 20
a, b = b, a
print(f"a={a} b={b}")
a, b, c = 1, 2, 3
print(f"a={a} b={b} c={c}")


def func():
    return 1, 2


a, b = func()
print(a, b)  # (1,2)

a = (1, 2, [3, 4])
a = [1, 2]
b = (1, 2, a)
a.append(8)
# (1, 2, [1, 2, 8]) #изменился не кортеж, а обект по ссылке а
print(b)
