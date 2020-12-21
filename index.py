
import csv
print("data is ")

with open('employee.csv', "r", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
