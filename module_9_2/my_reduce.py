from functools import reduce

reducing = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(reducing)  # 15 ((((1 +2)+3)+4)+5)
