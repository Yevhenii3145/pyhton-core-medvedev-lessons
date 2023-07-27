def mult(i):
    return i * 2


my_list = [1, 2, 3, 4, 5]
result = []

for i in my_list:
    element = mult(i)
    result.append(element)

print(result)  # [2, 4, 6, 8, 10]


result_of_maping = map(mult, my_list)
print(result_of_maping)  # <map object at 0x0000011B1CE9FF10>
# генератор можно перебрать только один раз
for i in result_of_maping:
    print(i, end=" ")  # 2 4 6 8 10
print("\n")

result_fo_maping_2 = map(lambda i: i * 2, my_list)
print(result_fo_maping_2)  # <map object at 0x0000015F8860FD60>
result_fo_maping_3 = (mult(i) for i in my_list)
print(result_fo_maping_3)  # <generator object <genexpr> at 0x0000015F885E0430>

for i in map(lambda i: i * 2, my_list):
    print(i, end=" ")  # 2 4 6 8 10
print("\n")

for key, value in map(lambda i: (i[0], i[1]), {"a": 1, "b": 2}.items()):
    print(key, value, end=" ")  # a 1 b 2
print("\n")


list_1 = [1, 2, 3, 4, 5]
list_2 = ["a", "b", "c", "d", "e"]

for n in map(lambda x, y: f"{y}: {x}", list_1, list_2):
    print(n, end=" | ")  # a: 1 | b: 2 | c: 3 | d: 4 | e: 5 |
