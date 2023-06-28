from pathlib import Path
my_path = Path("C:\\Users\\Admin\\Desktop\\_reset.scss")
print(my_path)  # "C:\Users\Admin\Desktop\_reset.scss"
print(my_path.suffix)  # .scss
print(my_path.exists())  # True (существует ли такой файл)

# False (поверка является ли обьект папкой)
print(my_path.is_dir())
# True (является лли файлом)
print(my_path.is_file())

my_path = Path("C:\\Users\\Admin\\Desktop\\")

for i in my_path.iterdir():
    print("i", i)
