class Record:
    def __init__(self, name):
        self.name = name


class Name:
    value = "Asd"


record = Record(Name())
print(record.name.value)  # Asd
