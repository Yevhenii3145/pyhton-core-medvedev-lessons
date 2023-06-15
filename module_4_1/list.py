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

my_list = ["a", "b", "c", "d", "e", "f"]

for i in range(len(my_list)):
    print(f'{i}-{my_list[i]}')  # 1-b 2-c 3-d 4-e 5-f

for index, element in enumerate(my_list):
    print(index, element)  # 0 a 1 b 2 c 3 d 4 e 5 f

for i in reversed(my_list):
    print(i)  # f e d c b a

for i in sorted(my_list):
    print(i)  # a b c d e f
