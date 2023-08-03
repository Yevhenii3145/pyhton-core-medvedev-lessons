# encapsulation, polymorphism, inheritance
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

    def damage_left(self):
        # в зависимости от оружия в right_hand метод kick_ass() будет выдавать разный результат - это есть полиморфизм
        self.left_hand.kick_ass()

    def damage_right(self):
        self.right_hand.kick_ass()

    def die(self):
        """gfdfghdfg"""
        drop_from_left, drop_from_right = self.left_hand, self.right_hand
        self.left_hand = None
        self.right_hand = None
        self.died = True
        return drop_from_left, drop_from_right


class Weapon:
    def __init__(self):
        self.damage = 10

    def kick_ass(self):
        print("Chik-chik")
        return self.damage


# атрибуты могут быть перезаписаны,унаследованы или свои собсственные(уникальные)
class Knife(Weapon):

    def __init__(self):
        self.damage = 5  # перезаписан (overwritten)
        self.weight = 12  # собственный (own)

    # kick_ass -унаследован (inherited)
    def throw(self):
        return self.damage - 2


class Sword(Weapon):

    def __init__(self):
        self.damage = 15

    def kick_ass(self):
        print("Slash-slash")
        return self.damage


class Axe(Knife):

    def __init__(self):
        self.damage = 20

    def kick_ass(self):
        print("Herak")
        return self.damage


class Gun(Weapon):
    def __init__(self):
        self.damage = 20

    def kick_ass(self):
        print("Baaaam")
        return self.damage


knife = Knife()
sword = Sword()
print(knife.kick_ass())  # 5
print(sword.kick_ass())  # 15
print(knife.throw())  # 3

char = Character("char")
sword = Sword()
char.pick_weapon(sword)
print(char.left_hand)  # <__main__.Sword object at 0x0000021A5A11FA00>
print(char.right_hand)  # <__main__.Weapon object at 0x000001E79C6EF9D0>
char.damage_left()  # Slash-slash
char.damage_right()  # Chik-chik
# абстрактные классы, интерфейсы, конракты, строгая типизация - это не соответствует философии python
