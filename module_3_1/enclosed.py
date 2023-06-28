def calculate_sum():
    x = 3
    y = 5

    def inner_func():
        nonlocal x
        print(x)  # 3
        x = 10
        print(x)  # 10

    inner_func()

    print("main", x)  # main 10
    return x + y


calculate_sum()
