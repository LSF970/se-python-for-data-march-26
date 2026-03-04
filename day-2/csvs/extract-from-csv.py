# Python script for extract data from a csv

# import csv library/module
import csv

# extract/import csv contents
rows = []
with open("employers.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(f"the headers are: {header}")
print(rows)


