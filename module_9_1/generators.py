# генераторы - это итераторы, но по которым можно итерироваться только 1 раз
def func():
    print("Entry point")
    yield None
    print("After yield")


print(func)  # <function func at 0x000002894E693E20>
print(func())  # <generator object func at 0x00000208B5010430>
next(func())  # Entry point
next(func())  # Entry point
# всегда будет entry poin т.к. мы не сохраняем состаяние генератора нигде
next(func())  # Entry point

generator = func()  # сохранили генератор в переменной
next(generator)  # Entry point
# next(generator)  # After yield # Traceback (most recent call last): StopIteration


def func_2(n):
    i = 0
    while i < n:
        print("Entry point")
        yield i
        print("After point")
        i += 1


generator_2 = func_2(5)
# next(generator_2)  # Entry point
# next(generator_2)  # After point Entry point
# next(generator_2)  # After point Entry point
# next(generator_2)  # After point Entry point
# next(generator_2)  # After point Entry point
# next(generator_2)  # After point Traceback (most recent call last): StopIteration


for element in generator_2:
    print(element)
# Entry point 0
# After point Entry point 1
# After point Entry point 2
# After point Entry point 3
# After point Entry point 4
# After point  и здесь цикл for ловит StopIteration
