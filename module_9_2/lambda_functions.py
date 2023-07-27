print(lambda x, y, z: x * y * z)  # <function <lambda> at 0x000002405E36FD00>
print((lambda x, y, z: x * y * z)(1, 2, 3))  # 6


def func(x, y, z):
    return x * y * z


result = func(1, 2, 3)
print(result)  # 6
print(func)  # <function func at 0x00000289B37CFD00>

# func_lambda = lambda x , y, z : x * y * z
# result_lambda = func_lambda(1, 2, 3)


def func_1(f):
    f()


func_1(lambda: print('Hello'))  # Hello

[(lambda i: print(i * 2, end=" "))(i) for i in range(5)]  # 0 2 4 6 8
