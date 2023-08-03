# Single responsibility
# association -composition & aggregation
class Character:

    hp = 100
    mp = 100

    def __init__(self, name, x=0, y=0):
        self.left_hand = None
        self.right_hand = Weapon()  # это композиция (один обьект является частью другого)
        self.name = name
        self.x = x
        self.y = y
        self.died = None

    def pick_weapon(self, weapon):
        if self.left_hand is None:
            self.left_hand = weapon
        elif self.right_hand is None:
            self.right_hand = weapon
        else:
            print("I am full")

    def show_weapon(self):
        return self.left_hand, self.right_hand

    def move(self: object) -> None:
        print("I am moving")

    def identify(self: object) -> None:
        print(self.name)

    def die(self):
        """gfdfghdfg"""
        drop_from_left, drop_from_right = self.left_hand, self.right_hand
        self.left_hand = None
        self.right_hand = None
        self.died = True
        return drop_from_left, drop_from_right


class Weapon:
    def __init__(self):
        self.type = "sword"
        self.damage = 10


char = Character("char")
# Opening a chest

sword_1 = Weapon()
char.pick_weapon(sword_1)

print(char.left_hand)  # <__main__.Weapon object at 0x0000018AEF2E3CD0>
print(char.right_hand)  # None
left_hand, right_hand = char.show_weapon()
# <__main__.Weapon object at 0x00000226833A3D00> None
print(left_hand, right_hand)
print(left_hand.type)  # sword
print(left_hand.damage)  # 10

char_1 = Character("char_1")
char_2 = Character("char_2")
sword = Weapon()
print(sword.type)  # sword

# тут происходит агрегация(собираем два не связанных обьекта)
char_1.pick_weapon(sword)
print(char_1.left_hand)  # <__main__.Weapon object at 0x000001C76530BBE0>
from_left_hand, from_right_hand = char_1.die()
print("char_1", char_1.left_hand, char_1.right_hand,
      char_1.died)  # char_1 None None True

char_2.pick_weapon(from_left_hand)  # тут происходит агрегация
print(char_2.left_hand)  # <__main__.Weapon object at 0x000001C76530BBE0>
