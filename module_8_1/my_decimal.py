from decimal import Decimal, getcontext

print(0.1 + 0.2 == 0.3)  # False

# указываем требуемую точность после знака
getcontext().prec = 2
print(Decimal(0.1) + Decimal(0.2))  # 0.30
print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3))  # False
print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3) + Decimal(0))  # True

print(Decimal(0.3))  # 0.299999999999999988897769753748434595763683319091796875
print(float(Decimal(0.3)))  # 0.3

print(round(0.234, 1))  # 0.2

print(float(Decimal(0.399999999)))  # 0.399999999
# 0.399999998999999994975240724670584313571453094482421875
print(Decimal(0.399999999))
