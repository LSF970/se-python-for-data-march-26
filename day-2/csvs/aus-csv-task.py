# Austrailian CSV tasks

import csv

# extract/import csv contents
rows = []
with open("aus.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(f"the headers are: {header}")
print(rows)

new_header = ['State', 'Population', 'Capital']
new_data = [["VIC","6649159", "Capital1"], ["NSW","8189266", "Capital2"], ["SA","1773243", "Capital3"], ["WA","2681633", "Capital4"], ["Tasmania","541479", "Capital5"], ["Queensland","5221170", "Capital6"], ["ACT","432266", "Capital7"], ["NT","246338", "Capital8"]]

# Add new column, write to file
with open("aus.csv", mode="w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(new_header) # add header data (columns)
    csvwriter.writerows(new_data) # add data (rows)

