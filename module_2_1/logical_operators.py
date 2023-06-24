# and or not
print(bool(1 and 1))  # True
print(bool(1 and 0))  # False
# оператор and запинается на неправде,если все операнды True - возвращает последнюю правду
print(1 and 1)  # 1
print(1 and 0)  # 0
print(0 and 1)  # 0
print(0 and 0)  # 0
print(1 and 2)  # 2
print(4 and 3)  # 3
print("a" and 8)  # 8
print("" and 3)  # ""
print("" and 0)  # ""
print(0 and "")  # 0
# оператор or запинается на первой правде, если все операнды False - возвращает последнюю неправду
print("" or 0)  # 0
print("abc" or True)  # "abc"
print("abc" or False)  # "abc"
print(False or 0)  # 0
print(0 or True)  # True
# оператор not преобразует значение в bool и возвращает обратоное полученному
print(not 0)  # True
print(not "")  # True
print(not False)  # True
print(not 1)  # False
print(not "abc")  # False
print(not True)  # False
