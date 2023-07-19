import random


print(random.randint(0, 210))  # 89

my_list = list(range(0, 10))
random.shuffle(my_list)
print(my_list)  # [8, 9, 5, 7, 6, 2, 1, 3, 4, 0]

ch = random.choice(my_list)
print(ch)  # 5
chs = random.choices(my_list, k=3)
print(chs)  # [4, 2, 3]

# TypeError: 'tuple' object does not support item assignment
# print(random.shuffle(tuple(my_list)))

print(random.choice(tuple(my_list)))  # 2


print(random.sample(my_list, k=4))  # [5, 6, 1, 0]
