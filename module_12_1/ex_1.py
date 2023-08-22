import pickle

print(bytes("asd".encode()))  # b'asd'

a = (1, 2, 3)
serialized = pickle.dumps(a)
# b'\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00K\x01K\x02K\x03\x87\x94.'
print(serialized)
deserialized = pickle.loads(serialized)
print(deserialized)  # (1, 2, 3)
print(a == deserialized)  # True
print(id(a))  # 2468512542016
print(id(deserialized))  # 2468512268352
