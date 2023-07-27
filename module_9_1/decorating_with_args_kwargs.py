import functools


def simple_decorator(func):

    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):

        print("Before func")
        result = func(*args, **kwargs)
        print("After func")
        return result

    return simple_wrapper


@simple_decorator
def func(text):
    print(text)


@simple_decorator
def mult(x, y):
    return x * y


func("asd")
mult(5, 6)

result = mult(3, 4)
print(result)  # Before func After func 12

# без functools.wraps
# print(mult)  # <function simple_decorator.<locals>.simple_wrapper at 0x000001FC9BFF4040>
# print(mult.__name__)  # simple_wrapper

# с functools.wraps
print(mult)  # <function mult at 0x000001E337D22320>
print(mult.__name__)  # mult
