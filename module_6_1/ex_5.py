print(type(b"asgkrt"))  # <class 'bytes'>

with open("text_4.txt", "w") as file:
    print(file.closed)
    file.write("Hello")
    raise ValueError
