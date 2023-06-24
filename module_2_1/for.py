print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# TypeError: 'in <string>' requires string as left operand, not int
# print(1 in "asd")

for i in range(0, 10):
    print(i, end="")  # 0123456789

for i in range(10):
    if i % 2:
        continue
    print(i, end="")  # 02468
