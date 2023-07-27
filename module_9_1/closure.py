def multiply(x):

    def inner(y):
        return x * y

    return inner


multiply_ten = multiply(10)
print(multiply_ten)  # <function multiply.<locals>.inner at 0x000001FF411AFB50>

print(multiply_ten(2))  # 20
print(multiply_ten(5))  # 50

multiply_three = multiply(3)
multiply_five = multiply(5)
print(multiply_ten(11))  # 110
print(multiply_three(11))  # 33
print(multiply_five(11))  # 55
