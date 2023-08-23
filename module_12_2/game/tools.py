import pickle
from entities import Character, Enemy, Portal

obj_map = {"Character": Character,
           "Enemy": Enemy,
           "Portal": Portal}


def load():
    with open(r"C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_12_2\game\save.bin", "rb") as file:

        game_state = pickle.load(file)

        objects = game_state["objects"]
        turns = game_state["turns"]
        size_m = game_state["size_m"]
        size_n = game_state["size_n"]

    return objects, size_n, size_m, turns


def save(objects, turns, size_m, size_n):
    game_state = {
        "objects": objects,
        "turns": turns,
        "size_m": size_m,
        "size_n": size_n
    }
    with open(r"C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_12_2\game\save.bin", "wb") as file:
        pickle.dump(game_state, file)
        # pickle.dump(objects, file)
        # pickle.dump(turns, file)
        # pickle.dump(size_m, file)
        # pickle.dump(size_n, file)
