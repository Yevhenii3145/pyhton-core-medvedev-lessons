for i in range(10):
    if i % 2:
        print(i, end=" ")  # 1 3 5 7 9
print("\n")

filtered = list(filter(lambda i: i % 2, range(10)))
print(filtered)  # [1, 3, 5, 7, 9]

for i in filter(lambda i: i % 2, range(10)):
    print(i, end="  ")  # 1  3  5  7  9
print("\n")


def func(text):
    if text in ("bad", "mad", "vodka", "beer"):
        return False
    return True


for i in filter(func, ["apple", "vodka", "potato", "beer"]):
    print(i, end="  ")  # apple  potato
print("")

bad_words = ["bad", "mad", "vodka", "beer"]

for i in filter(lambda i: i not in bad_words, ["apple", "vodka", "potato", "beer"]):
    print(i, end="  ")  # apple  potato
print("")
