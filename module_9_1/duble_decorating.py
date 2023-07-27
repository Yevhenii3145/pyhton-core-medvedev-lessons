import functools


def simple_decorator(func):

    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):

        print("Before func")
        result = func(*args, **kwargs)
        print("After func")
        return result

    return simple_wrapper


def simple_decorator_2(func):

    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):

        print("Before func 2")
        result = func(*args, **kwargs)
        print("After func 2")
        return result

    return simple_wrapper


@simple_decorator
@simple_decorator_2
def mult(x, y):
    print("Mult")
    return x * y


print(mult(3, 4))  # Before func| Before func 2| Mult| After func 2| After func| 12
