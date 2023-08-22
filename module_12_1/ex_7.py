import pickle


class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name)
        self.a = 123

    def read(self):
        return self.file.read()

    def __getstate__(self):
        attrs = self.__dict__.copy()  # делаем поверхностную копию дикта с атрибутами
        attrs["file"] = None
        return attrs

    def __setstate__(self, attrs):
        self.__dict__ = attrs
        # self.__dict__["file"] = open(self.file_name)
        self.file = open(self.file_name)


reader = Reader("test_5.csv")
# {'file': <_io.TextIOWrapper name='test_5.csv' mode='r' encoding='cp1251'>, 'a': 123}
print(reader.__dict__)
serialized = pickle.dumps(reader)
# b'\x80\x04\x95F\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x06Reader\x94\x93\x94)\x81\x94}\x94(\x8c\tfile_name\x94\x8c\ntest_5.csv\x94\x8c\x04file\x94N\x8c\x01a\x94K{ub.'
print(serialized)
deserialized = pickle.loads(serialized)
# <__main__.Reader object at 0x000001BC01073D50>
print(deserialized)
