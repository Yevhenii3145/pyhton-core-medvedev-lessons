from random import randint, choice

from tools import load, save
from game_map import generate_map, print_map


def generate_enemies(count):
    enemies = []
    for _ in range(count):
        enemy = {"x": randint(0, SIZE_N - 1),
                 "y": randint(0, SIZE_M - 1),
                 "sign": "E",
                 "type": "enemy",
                 "movable": True}
        enemies.append(enemy)
    return enemies


need_to_load = input("Do you want to load the game? (y/n): ")

if need_to_load.casefold() == "y":
    objects, SIZE_M, SIZE_N, turns = load()

else:
    SIZE_N = randint(20, 30)
    SIZE_M = randint(20, 30)
    char = {"x": randint(0, SIZE_N - 1),
            "y": randint(0, SIZE_M - 1),
            "sign": "X",
            "type": "char",
            "movable": True}

    portal = {"x": randint(0, SIZE_N - 1),
              "y": randint(0, SIZE_M - 1),
              "sign": "O",
              "type": "portal",
              "movable": False}
    enemies = generate_enemies(randint(10, 20))

    objects = [char, portal]
    objects.extend(enemies)
    turns = 0


def check_state(objects):
    for obj in objects:
        if obj["type"] == "char":
            char = obj
        elif obj["type"] == "portal":
            portal = obj
        elif obj["type"] == "enemy":
            loss_condition = char["x"] == obj["x"] and char["y"] == obj["y"]

            if loss_condition:
                char["sign"] = "L"
                print(f"You LOST in {turns} turns!")
                continue

    win_condition = char["x"] == portal["x"] and char["y"] == portal["y"]

    if win_condition:
        char["sign"] = "W"
        print(f"You WON in {turns} turns!")

    return win_condition or loss_condition


def move(direction, obj, size_m=SIZE_M, size_n=SIZE_N):
    if direction == "u" and obj["y"] > 0:
        obj["y"] -= 1
    elif direction == "d" and obj["y"] < size_m - 1:
        obj["y"] += 1
    elif direction == "l" and obj["x"] > 0:
        obj["x"] -= 1
    elif direction == "r" and obj["x"] < size_n - 1:
        obj["x"] += 1


def move_up(obj, size_m=SIZE_M, size_n=SIZE_N):

    if obj["y"] > 0:
        obj["y"] -= 1


def move_down(obj, size_m=SIZE_M, size_n=SIZE_N):

    if obj["y"] < (size_m - 1):
        obj["y"] += 1


def move_left(obj, size_m=SIZE_M, size_n=SIZE_N):

    if obj["x"] > 0:
        obj["x"] -= 1


def move_right(obj, size_m=SIZE_M, size_n=SIZE_N):

    if obj["x"] < (size_n - 1):
        obj["x"] += 1


def move_up_left(obj, size_m=SIZE_M, size_n=SIZE_N):
    if obj["y"] > 0 and obj["x"] > 0:
        obj["y"] -= 1
        obj["x"] -= 1


moves = {
    "u": move_up,
    "d": move_down,
    "l": move_left,
    "r": move_right,
    "ul": move_up_left
}


def get_move_handler(direction):
    return moves[direction]


while True:
    end_flag = check_state(objects)
    world_map = generate_map(objects, SIZE_M, SIZE_N)
    print_map(world_map)

    if end_flag:
        break

    for obj in objects:
        if obj["type"] == "char":
            direction = input("Enter direction (u / d / l /r): ")
            move_handler = get_move_handler(direction)
            move_handler(obj)
        elif obj["type"] == "enemy":
            enemy_direction = choice(("u", "d", "l", "r", "ul"))
            move_handler = get_move_handler(enemy_direction)
            move_handler(obj)
    turns += 1
    save(objects, turns, SIZE_M, SIZE_N)
