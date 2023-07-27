def decorator(func):

    def inner(*args, **kwargs):

        print("Before")
        result = func(*args, **kwargs)
        return result + 10

    return inner


@decorator
def func(x, y):
    return x + y


result = func(1, 2)
print(result)  # Before 13
