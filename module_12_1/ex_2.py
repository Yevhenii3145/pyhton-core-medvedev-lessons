import pickle

a = (1, 2, 3)

with open("test.bin", "wb") as file:
    pickle.dump(a, file)

with open("test.bin", "rb") as file:
    b = pickle.load(file)
