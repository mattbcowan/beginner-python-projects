# Best option for data structure is an array since we
# are only looking for the temps
arr = []

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(",")

        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid Temperature. Ignoring Row")

# Solve what is the average temp in the first week of Jan
print(sum(arr[0:7]) / len(arr[0:7]))
# Solve what was the maximum temp in the first 10 days of Jan
print(max(arr[0:10]))


# Best choice is dictionary for this because we are looking
# up by key to find the value
data = {}

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(",")

        try:
            temp = int(tokens[1])
            data[tokens[0]] = temp
        except:
            print("Invalid data. Skipped.")

# What was the temperature on Jan 9
print(data["Jan 9"])

# What was the temperature on Jan 4
print(data["Jan 4"])
