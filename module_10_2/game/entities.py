from config import Config


class Movable:
    movable = True

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.config = Config()

        self.moves = {
            "u": self.move_up,
            "d": self.move_down,
            "l": self.move_left,
            "r": self.move_right,
            "ul": self.move_up_left
        }

    def move_up(self):
        if self.y > 0:
            self.y -= 1

    def move_down(self):

        if self.y < (self.config.size_m - 1):
            self.y += 1

    def move_left(self):

        if self.x > 0:
            self.x -= 1

    def move_right(self):

        if self.x < (self.config.size_n - 1):
            self.x += 1

    def move_up_left(self):
        if self.y > 0 and self.x > 0:
            self.y -= 1
            self.x -= 1

    def move(self, direction):
        self.moves[direction]()


class NonMovable(Movable):
    movable = False


class Portal(NonMovable):
    sign = "O"


class Enemy(Movable):
    sign = "E"


class Character(Movable):
    sign = "X"
