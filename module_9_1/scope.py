# z is global skope, available in every place of this module
z = 1


def wrapper():
    # x is - not available
    # y is -local skope for wrapper
    y = 1

    def func(arg):
        # x is - local skope for func
        # y is - enclosed skope for func
        x = 1
        return arg

    return func


def func_1():
    print("Hello")


func_1()
