translate_map = {ord("є"): "ie", ord("і"): "y",
                 ord("q"): "й", ord("w"): "ц", ord("e"): "у", ord("r"): "к"}

new_string = "пєльмєні".translate(translate_map)
print(new_string)  # пieльмieнy
print("qwerty".translate(translate_map))  # йцукty
