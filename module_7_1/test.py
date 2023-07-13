# существует в пайтоне стандартная библиотека random, но мы создали модуль random и т.к. он находится ближе к нашему файлу чем стандартные библиотеки, импортируется именно он
import sys
import random
from my_package import new_func


# Hello из __init__.py
print(sys.path)  # ['c:\\Users\\Admin\\Desktop\\python-core-medvedev-lessons\\module_7_1', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
random.func()  # asd

new_func()
