import copy

a = [1, 2, 3]
print(id(a))  # 2435393926208
b = a
print(id(b))  # 2435393926208
print(a is b)  # True

b = a.copy()
print(id(a), id(b))  # 2143483671616 2143483625024
print(a is b)  # False

b = copy.copy(a)
print(id(a), id(b))  # 1175481306560 1175481099008


a = [1, 2, 3]
b = [a, 4, 5]
c = b
print(id(b), id(c))  # 2308820127168 2308820127168
print(b is c)  # True
b[0][0] = 99
print(b)  # [[99, 2, 3], 4, 5]
print(c)  # [[99, 2, 3], 4, 5]

c = copy.copy(b)
print(b)  # [[99, 2, 3], 4, 5]
print(c)  # [[99, 2, 3], 4, 5]
print(b is c)  # False

b[0][0] = 101
print(b)  # [[101, 2, 3], 4, 5]
print(c)  # [[101, 2, 3], 4, 5]
print(b is c)  # False
# хотя b и c это разные обекты но значение во вложенном списке изменелось на 101 одновременно
# 2657017214720 2657017214720 т.к. они оба ссылаются на a
print(id(b[0]), id(c[0]))
print(a)  # [101, 2, 3]

c = copy.deepcopy(b)
print(c, b)  # [[101, 2, 3], 4, 5] [[101, 2, 3], 4, 5]
print(id(b), id(c))  # 2050987626432 2050987460864
# 2050987407168 2050987469440 глубокая копия, ячейки разные
print(id(b[0]), id(c[0]))
print(id(a))  # 2050987407168
