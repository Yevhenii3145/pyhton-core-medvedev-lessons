# функция высшего порядка
def func(func):
    print(func)
    func()
    return func


def func_1():
    print("Hello")


x = func_1
func(x)  # <function func_1 at 0x000002A2899BFB50>  Hello
# <function func_1 at 0x000002A2899BFB50> Hello <function func_1 at 0x000002A2899BFB50>
print("Вызов", func(x))

a = func(x)
print("a", a)  # a <function func_1 at 0x000002A2899BFB50>
print(a())  # Hello None
