# public - открытый доступ
# protected - ограниченный доступ
# private - доступ есть только в классе

class Character:
    def __init__(self, name):
        self.name = name  # public
        self._damage = 10  # protected - доступ внутри класса и в наследниках класса
        self.__hp = 100  # private -доступ только внутри самого класса

    def func(self):
        print(self._damage)
        print(self.__hp)

    def public(self):
        pass

    def _protected(self):
        pass

    def __private(self):
        pass


class Enemy(Character):
    def func(self):
        print(self._damage)  # допускается т.к. это наследник класса  Character
        # print(self.__hp)  # не допусткается т.к. мы находимся внутри другого класса


char = Character("Jack")
char.name = "Vasya"
print(char.name)  # Vasya
char._damage = 12
print(char._damage)  # 12
# print(char.__hp) # AttributeError: 'Character' object has no attribute '__hp'
print(char.__dict__)  # {'name': 'Vasya', '_damage': 12, '_Character__hp': 100}
char._Character__hp = 120
print(char._Character__hp)  # 120
