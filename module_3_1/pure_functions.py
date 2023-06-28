x = 5


def calculate_sum():
    global x  # плохо т.к. функция работает с глобальной переменной x
    print("Calculation...", end=" ")
    y = 3
    x = x + y


print(calculate_sum())  # Calculation... None
print(x)  # 8
