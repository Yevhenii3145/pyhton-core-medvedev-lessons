class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = [self.x, self.y]

    def __str__(self):
        return f"str: ({self.x}, {self.y})"

    def __repr__(self):
        return f"repr: ({self.x}, {self.y})"

    def __getitem__(self, key):
        print(f"You are trying to get an element whith key {key} | ")
        return self.position[key]

    def __setitem__(self, key, value):
        if key in (0, 1):
            self.position[key] = value


char_position = Position(1, 3)
print(str(char_position))  # str: (1, 3)
print(char_position)  # str: (1, 3)
print(repr(char_position))  # repr: (1, 3)

print(char_position[0])  # You are trying to get an element whith key 0 |  1
