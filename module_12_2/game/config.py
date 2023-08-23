from random import randint


class Singleton:
    instance = None

    def __new__(class_):
        if not isinstance(class_.instance, class_):
            class_.instance = object.__new__(class_)
        return class_.instance


class Config(Singleton):
    def __init__(self):
        self.size_n = randint(10, 30)
        self.size_m = randint(10, 30)


# SIZE_N = 10  # randint(20, 30)
# SIZE_M = 10  # randint(20, 30)

# config_1 = Config()
# config_2 = Config()
# # config_1 и config_2 - это одно и то же
# print(config_1)  # <__main__.Config object at 0x000002BFDA29FDF0>
# print(config_2)  # <__main__.Config object at 0x000002BFDA29FDF0>
