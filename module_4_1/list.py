# cписок изменяемая, упорядоченная коллекция НЕ уникальных э-тов
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list = [1, 2, 3, "abc", False, None, 123]
print(list("My string"))
my_list = [1, 2, 3]
print(my_list[1])  # 2

a = [1, 2]
b = [3, 4, a]
print(b)  # [3, 4, [1, 2]]
print(b[2][0])
a[0] = 99
print(b)  # [3, 4, [99, 2]]
b.append("hello")
print(b)
