import pickle


class Character:
    def __init__(self, name):
        self.name = name


char = Character("Jack")

serialized = pickle.dumps(char)
print(serialized)  # b'\x80\x04\x95/\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tCharacter\x94\x93\x94)\x81\x94}\x94\x8c\x04name\x94\x8c\x04Jack\x94sb.'
deserialized = pickle.loads(serialized)
print(deserialized)  # <__main__.Character object at 0x00000206944934C0>
print(deserialized.name)  # Jack

with open("test.bin", "wb") as file:
    pickle.dump(char, file)

with open("test.bin", "rb") as file:
    b = pickle.load(file)
