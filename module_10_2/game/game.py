from random import randint, choice

from config import Config
from entities import Portal, Enemy, Character
from tools import load, save
from game_map import generate_map, print_map


need_to_load = input("Do you want to load the game? (y/n): ")
config = Config()

if need_to_load.casefold() == "y":

    objects, config.size_m, config.size_n, turns = load()

else:

    char = Character(randint(0, config.size_n - 1),
                     randint(0, config.size_m - 1))

    portal = Portal(randint(0, config.size_n - 1),
                    randint(0, config.size_m - 1))

    enemies = [Enemy(randint(0, config.size_n - 1),
                     randint(0, config.size_m - 1)) for _ in range(5)]

    objects = [char, portal]
    objects.extend(enemies)
    turns = 0


def check_state(objects):
    for obj in objects:
        if isinstance(obj, Character):
            char = obj
        elif isinstance(obj, Portal):
            portal = obj
        elif isinstance(obj, Enemy):
            loss_condition = char.x == obj.x and char.y == obj.y

            if loss_condition:
                char.sign = "L"
                print(f"You LOST in {turns} turns!")
                break

    win_condition = char.x == portal.x and char.y == portal.y

    if win_condition:
        char.sign = "W"
        print(f"You WON in {turns} turns!")

    return win_condition or loss_condition


while True:
    end_flag = check_state(objects)
    world_map = generate_map(objects, config.size_m, config.size_n)
    print_map(world_map)

    if end_flag:
        break

    for obj in objects:
        if isinstance(obj, Character):
            direction = input("Enter direction (u / d / l /r): ")
            obj.move(direction)
        elif isinstance(obj, Enemy):
            enemy_direction = choice(("u", "d", "l", "r", "ul"))
            obj.move(direction)
    turns += 1
    save(objects, turns, config.size_m, config.size_n)
