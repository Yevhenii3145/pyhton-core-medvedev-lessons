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
        return self.damage


# атрибуты могут быть перезаписаны,унаследованы или свои собсственные(уникальные)
class Knife(Weapon):

    def __init__(self):
        self.damage = 5  # перезаписан (overwritten)
        self.weight = 12  # собственный (own)

    # make_damage -унаследован (inherited)
    def throw(self):
        return self.damage - 2


class Sword(Weapon):

    def __init__(self):
        self.damage = 15


class Axe(Knife):

    def __init__(self):
        self.damage = 20


knife = Knife()
sword = Sword()
print(knife.kick_ass())  # 5
print(sword.kick_ass())  # 15
print(knife.throw())  # 3
