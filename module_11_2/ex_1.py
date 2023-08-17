class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # +
        if isinstance(other, Position):
            return ((self.x + other.x) ** 2 + (self.y + other.y) ** 2) ** 0.5
        elif isinstance(other, list):
            return other

    def __sub__(self, other):
        # -
        pass

    def __mul__(self, other):
        # *
        pass

    def __div__(self, other):
        # :
        pass

    def __eq__(self, other):
        # ==
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        # !=
        return not self.__eq__(other)

    def __lt__(self, other):
        # <
        pass

    def __gt__(self, other):
        # >
        pass

    def __le__(self, other):
        # <=
        pass

    def __ge__(self, other):
        # >=
        pass

    def __and__(self, other):
        # &
        pass

    def __or__(self, other):
        # |
        pass

    def __not__(self, other):
        # ^
        pass


char_position = Position(1, 1)
enemy_position = Position(3, 3)

print(char_position + enemy_position)  # 5.656854249492381
print(char_position + [3, 6, 7])  # [3, 6, 7]

#  ==  >  <  >=  <=  !=

print(char_position == enemy_position)  # False
enemy_position.x = 1
enemy_position.y = 1
print(char_position == enemy_position)  # True
