from copy import deepcopy

# print(help(list))

"""
    list.append(el)
    list.insert(i,el)
    list.remove(el)
    list.pop(i)
    list.index(el,s,e)
    list.count(el)
    list.reverse()
    list.extend(other_list)
    list.copy()
    list.clear()
    list.sort()
    list.sort(reverse=True)
    list.sort(key=func)

    sorted(list)
"""

a = [1, 2, 3]
a.clear()
print(a)

a = [1, 2]
b = [3, 4, a]
print(b)
a.append(5)
print(b)
c = b
print(c)
c = b.copy()  # делает поверхностную копию с ссылками
a[1] = 322
print(a)  # [1, 322, 5]
print(b)  # [3, 4, [1, 322, 5]]
print(c)  # [3, 4, [1, 322, 5]]

# заходит внутрь массива и рекуривно копирует
g = deepcopy(b)
a[2] = 555
print(a)  # [1, 322, 555]
print(b)  # [3, 4, [1, 322, 555]]
print(c)  # [3, 4, [1, 322, 555]]
print(g)  # [3, 4, [1, 322, 5]]

a = [1, 2, 2, 3, 4, 4, 4, 5, 4]
print(a.count(4))
a.extend([1, 2, 222])  # расширяем масив массивом
print(a)  # [1, 2, 2, 3, 4, 4, 4, 5, 4, 1, 2, 222]
a += [22, 66, 77, 55]

a = ["a", "b", "c"]
print(a.index("b"))  # 1

a = [1]
a.append([1, 2, 3])
print(a)  # [1, [1, 2, 3]]

a.insert(1, 99)  # 1-индекс 99- сам элемент
print(a)  # [1,99, [1, 2, 3]]

num = a.pop(0)  # pop(i)
print(num)  # 1

a = [1, 2, 1, 3]
# удалит элемент с первым вхождением слева
# если нет элемента будет ошибка
a.remove(1)
a.remove(max(a))
print(a)  # [2,1]

a = [1, 2, 3, 4, 5]
a.reverse()  # мутируем список разворачивая его в обратном порядке
print("reversed", a)

a.sort()
print("sorted", a)

# a = ["a","d", "c" ,2 ,4 ,5] енльзя равнивать строки и числа

a = ["g", "b", "c", "a"]
b = sorted(a)  # делает отсортированную копию
a.sort()  # мутирует список
print(a)  # ['a', 'b', 'c', 'g']
