
# the banned commands

import csv
with open("/Users/alfredarsenault/Downloads/fall_2029.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

