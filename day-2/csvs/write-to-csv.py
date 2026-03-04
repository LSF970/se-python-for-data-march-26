# Python script to write to a csv file

# import particular methods from csv library
from csv import writer

# Hardcode data
header = ['Name', 'Age']
data = [['Alex', 25], ['Brad', 30], ['Joey', 19]]

# open new file, write to that file
with open("student_info.csv", mode="w", newline="") as csvfile:
    csvwriter = writer(csvfile)
    csvwriter.writerow(header) # add header data (columns)
    csvwriter.writerows(data) # add data (rows)