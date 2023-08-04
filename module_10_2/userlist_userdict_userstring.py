from collections import UserDict, UserList, UserString
from random import randint


class MyList(UserList):
    def append(self, arg):
        print("Not yet")

    def get_data(self):
        print(f"Data: {self.data}")

    def update_with_random(self):
        self.data[0] = randint(0, 10)


l = MyList("asdasd")
l.append("f")  # Not yet
l.get_data()  # Data: ['a', 's', 'd', 'a', 's', 'd']

l.update_with_random()
l.get_data()  # Data: [7, 's', 'd', 'a', 's', 'd']
