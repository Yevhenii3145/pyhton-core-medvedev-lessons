class A:

    @staticmethod
    def method():
        print("asd")

    @classmethod
    def method_1(class_):
        print(class_)


a = A()
a.method()  # asd
A.method()  # asd
