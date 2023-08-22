import csv

with open("test_5.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# ['FirstName', 'LastName', 'Age', 'Sex']
# ['Jack', 'White', '21', 'M']
# ['John', 'Frusciante', '20', 'M']

with open("test_1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([1, 2, 3])
    writer.writerow([4, 5, 6])
