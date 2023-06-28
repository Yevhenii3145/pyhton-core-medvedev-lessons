def print_hello():
    print("Hello", end=" ")

    return


def print_bye():
    print('Bye', end=" ")

    return 'Bye'


def calculate_sum():
    x = 2
    y = 3

    return x + y if x > 5 else y


print(print_hello)  # <function print_hello at 0x000001673F5304A0>
print(print_hello())  # Hello None

result = print_bye()
print(result)  # Bye Bye
