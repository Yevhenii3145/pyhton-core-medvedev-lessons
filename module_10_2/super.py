class A:
    def __init__(self):
        print("Hello, I am A")


class B(A):
    def __init__(self):
        super().__init__()
        print("Hello, I am B")


a = A()  # Hello, I am A
b = B()  # Hello, I am A  Hello, I am B
