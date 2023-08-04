class list(list):

    def append(self, el):
        print("I can't do it")

    def say_hello(self):
        print(f"Hellof from {self}")


a = list("asdasd")
print(a)  # ['a', 's', 'd', 'a', 's', 'd']
a.append("c")  # I can't do it
