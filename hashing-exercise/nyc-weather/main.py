# Objectives:
# Solve what is the average temp in the first week of Jan
# Solve what was the maximum temp in the first 10 days of Jan

# Read CSV
import csv

file = open("nyc_weather.csv")
csvreader = csv.reader(file)

# Store the header info
header = []
header = next(csvreader)

# Add CSV Data to HashTable
data = {}
for row in csvreader:
    data[row[0]] = int(row[1])

print(data)
