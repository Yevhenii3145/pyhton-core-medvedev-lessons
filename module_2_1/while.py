count = 0
while count < 3:
    print("Hello")
    count += 1
print("End")


i = 0
while True:
    print(i, end="")  # 01234
    i += 1
    if i == 5:
        break

# редко встречающаяся конструкция while else
a = 2
while a == 1:
    print(1)
    break
else:
    print("else", 2)  # else 2
