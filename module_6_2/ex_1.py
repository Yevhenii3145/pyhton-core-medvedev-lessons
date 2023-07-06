file = open("name.txt", "w")
file.close()

with open("file.txt", "w") as f:
    f.write("Hello world")
f.close()

print("asd".encode())  # b'asd'
print(list(bytearray(b"asd")))  # [97, 115, 100]
