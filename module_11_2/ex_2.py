class str(str):
    def __add__(self, other):
        return 1

    # переопределяем метод ==
    def __eq__(self, other):
        print(type(self), type(other), "|")

        if isinstance(other, int):
            print(type(self), type(other.__str__()), "|")
            return super().__eq__(other.__str__())


a = str("a")
b = str("b")

c = "c"

print(type(a))  # <class '__main__.str'>
print(type(c))  # <class 'str'>

print(a + c)  # 1
print(c + a)  # ca
print(a + b)  # 1

# <class '__main__.str'> <class 'int'> | <class '__main__.str'> <class 'str'> | True
print(str("1") == 1)
