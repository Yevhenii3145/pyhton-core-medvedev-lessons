TEMP = 10


def func():
    print("Hello", end=" ")
    print(__name__)


if __name__ == '__main__':  # точка входа
    print("abc")
    func()  # Hello __main__
