import re
text = """Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.

This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.

For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth."""

symbol_to_exclude = (',', '.', '!')
normalized_text = text.lower()

# 1 вариант
# for symbol in symbol_to_exclude:
#     normalized_text.replace(symbol, '')

# 2 вариант
# for char in normalized_text:
#     if not char.isalnum():
#         normalized_text = normalized_text.replace(char, "")

# 3 вариант
reg_exp = r'[^a-zA-Z0-9 ]'
normalized_text = text.lower()
# убираем запятые и точки
normalized_text = re.sub(reg_exp, '', normalized_text)
print(normalized_text)

words_list = normalized_text.split()
unique_words_list = set(words_list)
n_words = len(words_list)
n_unique_words = len(set(words_list))
print(n_words)
print(n_unique_words)

words_dictionary = {}

for word in unique_words_list:
    words_dictionary[word] = normalized_text.count(word)
print(words_dictionary)

# превращаем в список, чтобы ипользовать далее метод sort
words_dictionary_list = list(words_dictionary.items())
print(words_dictionary_list)


def get_count(element):
    return element[1]


words_dictionary_list.sort(key=get_count)
# получим отортированный список кортежей по возротанию  [('examples', 1), ('gives', 1), ('powerful', 1),....]
print(words_dictionary_list)
