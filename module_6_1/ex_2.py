file = open("text_2.txt", "r")

for line in file:
    print(line)

file.close()

file = open("text_2.txt", "a")
file.write("asdasasdasd\n")
file.write("asdasasdasd\n")
file.write("asdasasdasd")
file.write("asdasasdasd")
file.close()
