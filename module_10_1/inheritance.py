class A:
    def hello(self):
        print("hello from A")


class B(A):
    pass


class C:
    def hello(self):
        print("hello from C")


class D(B, C):
    pass


# интерпретатор зайдёт в B не найдёт метод hello(), зайдет вертикально в A
# и там найдёт метод, т.к. B наследуеся от A
print(D().hello())  # hello from A None
