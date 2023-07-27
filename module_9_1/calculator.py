x = int(input("X: "))
y = int(input("Y: "))
operator = input("Operator: ")


def operate(x, y, operator):
    if operator == "+":
        result = x + y
    elif operator == "*":
        result = x * y
    elif operator == "-":
        result = x - y
    print(result)
    return result


operate(x, y, operator)
