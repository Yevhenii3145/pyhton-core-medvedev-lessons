class Position:
    def __init__(self, x, y):
        # self.__str__ = "abc"
        self.x = x
        self.y = y
        self.position_list = [self.x, self.y]
        self.position_dict = {"x": self.x, "y": self.y}

    def __str__(self):
        return f"str: ({self.x}, {self.y})"

    def __repr__(self):
        return f"repr: ({self.x}, {self.y})"

    def __getitem__(self, key):
        print(f"You are trying to get an element whith key {key} | ")
        return self.position_list[key]

    def __setitem__(self, key, value):

        if isinstance(key, str):
            self.position_dict[key] = value
        elif isinstance(key, int):
            if key == 0:
                self.x = value
                self.position_list[key] = value
            elif key == 1:
                self.y = value
                self.position_list[key] = value
            else:
                pass
            #     raise ValueError("Index could be either 0 or 1")
            # если ключ больше чем индекс последнего элемента
            if key > len(self.position_list) - 1:
                self.position_list.append(value)
            if 1 < key <= len(self.position_list) - 1:
                self.position_list[key] = value
            # self.position_list[key] = value

    def __call__(self, a):

        print("This object has been called")
        print(a)
        print(f"{self.position_list}")

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Finishing context manager")

        if exc_type is not None:
            print(
                "There was an exception: {exc_type}: {exc_value}\n{traceback}")
            # raise exc_type(exc_value)


char_position = Position(1, 3)
print(str(char_position))  # str: (1, 3)
print(char_position)  # str: (1, 3)
print(repr(char_position))  # repr: (1, 3)

print(char_position[0])  # You are trying to get an element whith key 0 |  1
print(char_position.position_list)  # [1, 3]
char_position[0] = 2
print(char_position.position_list)  # [2, 3]
# char_position[4] = 13  # ValueError: Index could be either 0 or 1
char_position["x"] = 5
print(char_position.position_dict)  # {'x': 5, 'y': 3}
print(char_position.position_list)  # [2, 3]
char_position[2] = 11
print(char_position.position_list)  # [2, 3, 11]
char_position[2] = 33
print(char_position.position_list)  # [2, 3, 33]
char_position[5] = 445
print(char_position.position_list)  # [2, 3, 33, 445]
char_position[2] = 9
char_position[3] = 66
print(char_position.position_list)  # [2, 3, 9, 66]

char_position(22)  # This object has been called  22  [1, 3, 9, 66]

with char_position as c_p:
    # raise ValueError("asdsadassd")
    print(c_p)  # Entering the context  str: (2, 3)  Finishing context manager
