my_list = []

for i in range(10):
    if i % 2:
        my_list.append(i * 10)

print(my_list)  # [10, 30, 50, 70, 90]

my_list_comp = [i * 10 for i in range(10) if i % 2]
print(my_list_comp)  # [10, 30, 50, 70, 90]

# [compr(i) for i in iterable if condition]

my_list_comp = [i * 10 if i % 2 else 123 for i in range(10)]
print(my_list_comp)  # [123, 10, 123, 30, 123, 50, 123, 70, 123, 90]

my_dict = {i: el for i, el in enumerate(["a", "b", "c"])}
print(my_dict)  # {0: 'a', 1: 'b', 2: 'c'}

my_set = {i for i, el in enumerate(["a", "b", "c"])}
print(my_set)  # {0, 1, 2}
