def func(arg):
    print(arg)


print(func)  # <function func at 0x0000028C8921FD00>
a = (func)
print(a)  # 0x0000028C8921FD00

print(func("asd"))  # asd None
print(a("asd"))  # asd None
