# словарь -неупорядоченная, изменяема коллекция уникальных пар элементов
# print(help(dict))
new_dict = {"key": "value", "key_1": "value_1"}
print(len(new_dict))  # 2

# ключи вегда уникальные и это должны быть хешируемые(неизменяемые) обьекты
# print(hash([1, 2, 5])) TypeError: unhashable type: 'list'

a = {1: 1, 2: 2, "a": 4}
# print(a[5]) KeyError: 5
print(a.get(5))  # None - но ошибки не будет

a = {"a": 1, "b": 2, "c": 3}
print(a.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(a.keys())  # dict_keys(['a', 'b', 'c'])
print(a.values())  # dict_values([1, 2, 3])

a = {"a": 1, "b": 2, "c": 3}

for key, value in a.items():
    print(key, value)  # a 1   b 2   c 3
