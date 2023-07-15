def load():
    # 14 14 X char
    objects = []
    with open(r"C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_6_2\save.txt", "r") as file:

        for i, line in enumerate(file):
            if i == 0:
                map_size = line.strip().split()
                size_n, size_m = int(map_size[0]), int(map_size[1])
            elif i == 1:
                turns = int(line.strip())
            else:
                data = line.strip().split()

                obj = {}
                obj["x"] = int(data[0])
                obj["y"] = int(data[1])
                obj["sign"] = data[2]
                obj["type"] = data[3]
                objects.append(obj)

    return objects, size_m, size_n, turns


def save(objects, turns, size_m, size_n):
    with open(r"C:\Users\Admin\Desktop\python-core-medvedev-lessons\module_6_2\save.txt", "w") as file:

        file.write(f"{size_n} {size_m}\n")
        file.write(f"{turns}\n")

        for obj in objects:
            x, y, sign, type1 = obj["x"], obj["y"], obj["sign"], obj["type"]
            file.write(f"{x} {y} {sign} {type1}\n")
