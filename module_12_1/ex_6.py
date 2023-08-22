import csv

with open("test_6.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
# {'FirstName': 'Jack', 'LastName': 'White', 'Age': '21', 'Sex': 'M'}
# {'FirstName': 'John', 'LastName': 'Frusciante', 'Age': '20', 'Sex': 'M'}
# {'FirstName': 'Mark', 'LastName': 'Ramone', 'Age': '', 'Sex': 'M'}
# {'FirstName': 'Max', 'LastName': None, 'Age': None, 'Sex': None}
# {'FirstName': '1', 'LastName': '2', 'Age': '3', 'Sex': '4', None: ['5', '6', '7', '8']}

with open("test_6_2.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, delimiter=";", fieldnames=[
                            "first_name", "last_name"])

    writer.writeheader()

    writer.writerow({"first_name": "Jack", "last_name": "White"})
    writer.writerow({"first_name": "John", "last_name": "Frusciante"})
