new_str = "{} {} {} {}".format("a", "b", "c", "d")
print(new_str)  # a b c d

new_str = "{0} {2} {1} {3} {0}".format("a", "b", "c", "d")
print(new_str)  # a c b d a
new_str = "{name} {last_name}".format(name="John", last_name="Frusciante")
print(new_str)  # John Frusciante
new_str = "{0:d} {0:#b} {0:#x} {0:#o}".format(10)
print(new_str)  # 10 0b1010 0xa 0o12
a = 10
print(f"{int(a)} {hex(a)} {bin(a)} {oct(a)}")  # 10 0xa 0b1010 0o12

print("{0:*^10}".format("asd"))  # ***asd****
print("{0:*<10}".format("asd"))  # asd*******
print("{0:*>10}".format("asd"))  # *******asd
