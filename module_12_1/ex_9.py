from copy import copy, deepcopy


class Character:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.bag = ["potion", "money"]

    def add_to_bag(self, item):
        self.bag.append(item)

    def __copy__(self):
        char = Character(self.name)
        return char

    def __deepcopy__(self, memo):
        obj = Character(self.name)
        memo[id(self)] = obj

        for k, v in self.__dict__.items():
            setattr(obj, k, deepcopy(v, memo))

        return obj


char = Character("Jack")
char.add_to_bag(["magic apple", "beer"])
print(char.bag)  # ['potion', 'money', ['magic apple', 'beer']]

print(char)  # <__main__.Character object at 0x000001E2FB953FD0>
char_copy = copy(char)
print(char_copy)  # <__main__.Character object at 0x000001E2FB953E20>

char_1 = deepcopy(char)
print(char_1.bag)  # ['potion', 'money', ['magic apple', 'beer']]
print(id(char.bag[2]))  # 2141693949824
print(id(char_1.bag[2]))  # 2141693686272
