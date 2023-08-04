from entities import Character, Enemy, Portal

obj_map = {"Character": Character,
           "Enemy": Enemy,
           "Portal": Portal}


def load():
    objects = []
    with open(r"C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_10_2\game\save.txt", "r") as file:

        for i, line in enumerate(file):
            if i == 0:
                map_size = line.strip().split()
                size_n, size_m = int(map_size[0]), int(map_size[1])
            elif i == 1:
                turns = int(line.strip())
            else:
                data = line.strip().split()

                obj = obj_map[data[2]](int(data[0]), int(data[1]))
                objects.append(obj)

    return objects, size_m, size_n, turns


def save(objects, turns, size_m, size_n):
    with open(r"C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_10_2\game\save.txt", "w") as file:

        file.write(f"{size_n} {size_m}\n")
        file.write(f"{turns}\n")

        for obj in objects:
            file.write(f"{obj.x} {obj.y} {type(obj).__name__}\n")
