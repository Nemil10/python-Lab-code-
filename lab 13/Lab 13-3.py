import csv

with open(r"C:\Users\student\Downloads\Example1.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
