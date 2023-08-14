class Character:
    def __init__(self, name):
        self.name = name  # public
        self._damage = 10  # protected
        self.__hp = 100  # private

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        if 0 <= hp <= 100:
            self.__hp = hp

    @property
    def hp(self):
        print("GETTER")
        return self.__hp

    @hp.setter
    def hp(self, value):
        print("SETTER")
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError("HP should be in range 1-100")


char = Character("Jack")
# char.__hp # AttributeError: 'Character' object has no attribute '__hp'
print(char.get_hp())  # 100
char.set_hp(90)
print(char.get_hp())  # 90
char.set_hp(1000)
print(char.get_hp())  # 90

char = Character("Nick")
print(char.hp)  # GETTER 100
char.hp = 50  # SETTER
print(char.hp)  # GETTER 50
# char.hp = 500  # SETTER # ValueError: HP should be in range 1-100
