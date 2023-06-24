while True:
    user_input = input("Enter number: ")
    try:
        x = int(user_input)
    except ValueError:
        print("Should be a number. Please try again!")
        continue
    break

while True:
    user_input = input("Enter number: ")
    try:
        x = int(user_input)
    except ValueError as error:
        print("Value", error)
    except TypeError:
        print("Type")
        continue
    else:
        # выполнится в случае, если не было ошибки
        print("Else")
    finally:
        print("Finally")  # выполнится в любом случае
    break
