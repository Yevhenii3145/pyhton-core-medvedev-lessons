with open("text_6.txt", "wb") as file:
    file.write(b"agjftl")

with open("text_6.txt", "r") as file:
    print(file.read())

print(bytes([0, 0, 0]))  # b'\x00\x00\x00'

print("abcd".encode("utf-8"))  # b'abcd'
b_array = bytearray(b"asrths")
print(list(b_array))  # [97, 115, 114, 116, 104, 115]
print(ord("a"))  # 97
b_array[2] = ord("f")
print(list(b_array))  # [97, 115, 102, 116, 104, 115]
