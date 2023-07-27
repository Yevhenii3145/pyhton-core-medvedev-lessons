import functools


def decor_with_args(arg):

    def simple_decorator(func):

        @functools.wraps(func)
        def simple_wrapper(*args, **kwargs):

            print(f"Before {arg}")
            result = func(*args, **kwargs)
            print(f"After {arg}")
            return result

        return simple_wrapper

    return simple_decorator


@decor_with_args("asd")
def mult(x, y):
    print("Mult")
    return x * y


print(mult(5, 6))  # Before asd  Mult  After asd  30
