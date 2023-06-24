# нельзя int начинать с 0, кроме случаев с несколькими 0
initial_pin = "0123"
max_tries = 3

n = 0
# т.к. мы не знаем изначально  какой попытки введут правильный пароль, и здесь нет итерации по чему-либо то лучше while
while n < max_tries:
    user_pin = input("Enter your pin: ")

    if len(user_pin) == 4 or len(user_pin) == 6:
        if initial_pin == user_pin:
            amount = input("How much: ")
            if amount > 0:
                print("Take your {amount}")
                break
        else:
            print("Sorry, wrong pin. Try again please!")
            n += 1
            print(f"You have {max_tries - n} tries")
    else:
        print("Pin should be 4 or 6 digits.")
print("Good bye!")


# всё таки если через for
for i in range(3):
    user_pin = input("Enter your pin: ")

    if len(user_pin) == 4 or len(user_pin) == 6:
        if initial_pin == user_pin:
            print("Here's you money")
            break
        else:
            print("Sorry, wrong pin. Try again please!")
    else:
        print("Pin should be 4 or 6 digits.")
print("Good bye!")
