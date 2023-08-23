from copy import copy


class Users:
    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)

    def __copy__(self):
        my_users_copy = Users()
        my_users_copy.user_list = [copy(user) for user in self.user_list]
        return my_users_copy


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __copy__(self):
        users_copy = User(self.name, self.age)
        return users_copy


user_1 = User("Jack", 19)
user_2 = User("John", 20)

users = Users()
users.add_user(user_1)
users.add_user(user_2)

print(id(users))  # 1984980401168
users_copy = copy(users)
print(id(users_copy))  # 1743765584240

# [<__main__.User object at 0x0000020AA3C83FD0>, <__main__.User object at 0x0000020AA3C83D60>]
print(users.user_list)
# [<__main__.User object at 0x000001FB68618430>, <__main__.User object at 0x000001FB68618370>]
print(users_copy.user_list)
