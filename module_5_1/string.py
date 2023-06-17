# help(str)
single_line_str = 'the firs line'\
                  'the second line'\
                  'the third line'

string = "sf" "sdgg" "sdgo"
print(string)  # sfsdggsdgo
my_str = 'the first line\nthe second line'
print(my_str)
new_str = 'the first line\'the second line'
print(new_str)

# сырая трока, отображаетя как еть  C:\new_folder\xxx\ta
raw_str = r'C:\new_folder\xxx\ta'
print(raw_str)

print("hello hello".capitalize())  # Hello hello
print("Hello hello".casefold())  # hello hello
print("hello".center(10, "*"))  # **hello***
print("hello".count("l", 0, 4))  # 2 -количетво совпадений
print("hello".endswith("lo", 0, 5))  # True
# индекс вхождения подстроки в строку
print("hello".find("lo"))  # 3
print("hello".find("gt"))  # -1  не нашёл
print("hello".index("lo"))  # 3
# print("hello".index("gt")) #ValueError: substring not found
print("hello hello".title())  # Hello Hello
# состоит только из букв и цифр
print("asd12".isalnum())  # True

# проверка является ли строка идентификатором
print("break".isidentifier())  # True
print("***".join(["a", "b", "c"]))  # a***b***c
print("    hello   ".lstrip())  # "hello   "
print("hellllllllllllooo".partition("l"))  # ('he', 'l', 'lllllllllllooo')

# ['he', '', '', '', '', '', '', '', '', '', '', '', 'ooo']
print("hellllllllllllooo".split("l"))
