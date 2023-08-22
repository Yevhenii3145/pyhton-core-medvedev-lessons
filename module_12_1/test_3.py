import pickle


class Character:
    def __init__(self, name):
        self.name = name

    def asd(self):
        print("gg")
        pass


with open("test.bin", "rb") as file:
    deserialized = pickle.load(file)
    # если в этом (принимающем) файле нет класса Character с такими-же полями, то будет ошибка
    # print(deserialized)  # AttributeError: Can't get attribute 'Character' on <module '__main__' from 'C:\\Users\\Admin\\Desktop\\python-core-medvedev-lessons\\module_12_1\\test_3.py'>
    print(deserialized)  # <__main__.Character object at 0x000001C7ED55D150>
