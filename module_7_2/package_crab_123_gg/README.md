This is a file with my package description

# https://packaging.python.org/en/latest/tutorials/packaging-projects/

# https://choosealicense.com/

Команда для создания сборки пакета
запускаем в терминале предварительно зайдя в родительскую папку например my_new_package

# python -m build

Всё также находясь в родительской папке пакета пишем команду

Для windows

# py -m pip install --upgrade twine

Чтобы залить в тестовый репозиторий пакетов прописываем

# py -m twine upload --repository testpypi dist/\*
