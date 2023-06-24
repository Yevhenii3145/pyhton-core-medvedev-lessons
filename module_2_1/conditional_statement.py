print("Start")
if bool(True):
    print("Hello")
    print("World")
    if not False:  # not False = True
        print("123")
print("End")

"""
Start
Hello
World
123
End"""

user_name = input("Enter your name: ")

if user_name == "Alex":
    print("Hello Alex")
elif user_name == "Vasya":
    print("Hello Vasya")
elif user_name == "Masha":
    print("Hello Masha")
else:
    print("Wrong user name!")
print("End")
