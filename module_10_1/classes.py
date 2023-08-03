class Character:

    name = None
    x = None
    y = None
    hp = 100
    mp = 100

    def move(self: object) -> None:
        """docstring"""
        print("self", self)
        print("I am moving")

    def identify(self: object) -> None:
        print(self.name)

    def new_f(self: object) -> None:
        self.identify()

    def die(self):
        # дописываем новую характеристику для экземпляра
        self.dead = True


char = Character()
print(char)  # <__main__.Character object at 0x0000027F815C3580>
char_1 = Character()
char_2 = Character()
print(char_1)  # <__main__.Character object at 0x0000027F815C3550>
print(char_2)  # <__main__.Character object at 0x0000027F815C3520>
print(char_1.hp)  # 100
print(char_1.name)  # None
print(char_2.mp)  # 100
char_1.name = "Edelweiss"
char_2.name = "Габриэль"
print(char_1.name)  # Edelweiss
print(char_2.name)  # Габриэльc
# Меняем классовую характеристику hp
Character.hp = 300
print(char_1.hp)  # 300
print(char_2.hp)  # 300
# Меняем классвую характеристику name, но значения в обьектах не изменятся
# т.к мы переопределяли поле [name] для объектов char_1 и char_2
Character.name = "asd"
print(char_1.name)  # Edelweiss
print(char_2.name)  # Габриэль
char_3 = Character()
print(char_3.name)  # asd взял дефолтное изменённое значение
# Если мы перезаписали какую-то характеристику класса, она перестаёт зависеть от класса!

Character.name = "Gadzila"
char_4 = Character()
print(char_4)  # <__main__.Character object at 0x0000027C75373E50>
# self - это есть сам экземпляр класса для которого мы вызываем метод
char_4.move()  # self <__main__.Character object at 0x0000027C75373E50> I am moving
char_4.identify()  # Gadzila
char_4.name = "Script"
print(char_4.name)  # Script
char_4.new_f()  # Script
# print(char_4.dead) # AttributeError: 'Character' object has no attribute 'dead'
# дописываем экземпляру свойство die
char_4.die()
print(char_4.dead)  # True
