import csv

with open('members.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['first_name']} {row['last_name']}")
