class Character:

    count = 0
    hp = 100
    mp = 100

    def __init__(self, name, x, y):
        print("Init")
        Character.count += 1
        self.name = name
        self.x = x
        self.y = y

    def move(self: object) -> None:
        """docstring"""
        print("self", self)
        print("I am moving")

    def identify(self: object) -> None:
        print(self.name)


char_1 = Character("First", 1, 1)  # Init
char_2 = Character("Second", 2, 2)  # Init
print(Character.count)  # 2

char_3 = Character("Alex", 0, 0)  # Init
print(char_3.name)  # Alex
