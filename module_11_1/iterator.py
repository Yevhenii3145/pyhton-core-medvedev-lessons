class Iterator:

    def __init__(self):
        self.start = 5

    def __next__(self):
        print(f"Hey, I am iteration number {self.start}")
        self.start += 1

        if self.start == 101:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


iterator = Iterator()

for i in iterator:
    print(i)
