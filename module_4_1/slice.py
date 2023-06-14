my_list = [1, 2, 3, 4, 5, 6]
s = my_list[1:3:1]
print(s)  # [2, 3]
print("Hello world"[0:-1:2])  # Hlowr
print("Hello world"[:])  # ~ [0:len:1] start stop step

a = [1, 2, 3, 4, 5]
b = a[1:4]
print(b)
b.append(7)
print(b)
print(a)
