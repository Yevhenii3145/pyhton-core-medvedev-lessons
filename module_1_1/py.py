import this
print(this)


def func():
    pass


print(func)  # <function func at 0x00000208D70104A0>
# числа ссылаются на одну и ту же ячейку памяти
a = 999
print(id(a))  # 140737285706536
b = 999
print(id(b))  # 140737285706536
print(a is b)  # True
a = [1, 2]
b = [1, 2]
# списки даже с одинаковыми значениями внутри, ссылаются на разные ячейки
print(id(a))  # 1273391893248
print(id(b))  # 1273391892672
print(a == b)  # True
print(a is b)  # False
a = [1, 2]
b = a
print(a == b)  # True
print(a is b)  # True

camelCase = ""
# kebab-case = ""
# в Python используются в основном
snake_case = ""
SCREAMING_SNAKE_CASE = ""
PascalCase = ""
