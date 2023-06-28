def calculate_sum(x, y):
    return x + y


result = calculate_sum(5, 5)
print(result)


def calculate_diff(x, y, z):
    return x - y - z


# порядковые аргуметы идут раньше именованых
result = calculate_diff(2, z=5, y=10)
print(result)  # -13


def calculate_diff_2(x, y=5):
    return x - y


result = calculate_diff_2(2, 10)
print(result)  # -8


def position_args(*args):
    for arg in args:
        print(arg, end=" ")
    return args


result = position_args(1, 2, 3, 4, 12, 7, 8, 9)
print(result)  # 1 2 3 4 12 7 8 9 (1, 2, 3, 4, 12, 7, 8, 9)


def named_args(**kwargs):
    return kwargs


result = named_args(a="5", b="10", c="20")
print(result)  # {'a': '5', 'b': '10', 'c': '20'}


def all_args(x, y, *args, a=5, **kwargs):
    print(args, end=" ")  # (3,)
    print(kwargs, end=" ")  # {'b': 10, 'c': 22}
    return (x, y, a)


result = all_args(1, 2, 3, a=11, b=10, c=22)
print(result)  # (3,) {'b': 10, 'c': 22} (1, 2, 11)
