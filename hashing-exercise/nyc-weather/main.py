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

# Function to get average temperature between certain days
def get_average_temp(month, start_day, end_day):
    total_temp = 0

    # Iterate over days between the start and end day
    # ISSUE: WHAT IF WEEK IS BETWEEN MONTHS? EX: Jan 29 - Feb 4
    for day in range(start_day, end_day + 1):
        date = month + " " + str(day)
        print(date)
        total_temp += data[date]

    # Get the total temp and divide by days of the week
    # Limit decimal places to 1 place for ease of reading
    avg_temp = round(total_temp / (end_day - start_day), 1)
    return avg_temp


print(get_average_temp("Jan", 1, 7))
