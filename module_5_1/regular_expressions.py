import re
# help(re)
# regex101.com

url_regexp = r'https?:\/\/(www\.)?[-a-z-A-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-z-A-Z0-9()@:%_\+.~#?&//=]*)'

result = re.search(
    url_regexp, 'You can search some info: https://www.google.com sdgffdsdg')
print(result)  # <re.Match object; span=(26, 48), match='https://www.google.com'>
print(type(result))  # <class 're.Match'>
print(result.group())  # https://www.google.com

result = re.findall(
    url_regexp, "You can search some info: https://www.google.com sdgffdsdg https://www.google.com")
print(result)
ip_regexp = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
result = re.search(ip_regexp, "255.255.11.145")
print(result)  # <re.Match object; span=(0, 14), match='255.255.11.145'>

my_simple_regexp = r'.\d'
result = re.search(my_simple_regexp, "a1 asd 10")
print(result.group())  # a1
result = re.findall(my_simple_regexp, "a1 asd &46")
print(result)  # ['a1', '&4']

# заменит все найденные по паттерну подстроки на *
a = re.sub(my_simple_regexp, "*", "a1 asd &46")
print(a)  # * asd *6
