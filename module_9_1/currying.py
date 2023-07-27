from math import cos

# (solid) functions are open to extensions, and closed to modifications


def summ(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


operations = {"+": summ, "*": mul, "-": sub, "cos": cos}

print(operations["+"])  # <function summ at 0x0000019D3F903E20>
print(operations["+"](5, 10))  # 15


def operate(operator):
    return operations[operator]


handler_sum = operate("+")

print(handler_sum(2, 3))  # 5
print(operate("+")(2, 3))  # 5
print(handler_sum(2, 3) == operate("+")(2, 3))  # True


print(operate("cos")(30))  # 0.15425144988758405
