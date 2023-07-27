def multiply(x):
    def inner(y):
        def func(z):
            return x * y * z
        return func
    return inner


multiply_10 = multiply(10)  # x = 10
print(multiply_10)  # <function multiply.<locals>.inner at 0x00000258FC05FB50>
multiply_10_3 = multiply_10(3)  # x = 10 y = 3

# <function multiply.<locals>.inner.<locals>.func at 0x000001ECBB1FFBE0>
print(multiply_10_3)
print(multiply_10_3(4))  # 120 # x = 10 y = 3 z = 4

print(multiply(10)(3)(4))  # 120 # x = 10 y = 3 z = 4
