import pandas as pd
import sys


# manually set hour
hour = sys.argv[1]
hours = sys.argv[2]

print(len(sys.argv))

print(hour, hours)


def lin(hour, i):
    lin = "files/" + str(int(hour) + i) + "/quotes.csv"
    return lin


# read 4 csv files and concat into one
a = pd.read_csv("files/" + str(hour) + "/quotes.csv")

for i in range(int(hours)):
    b = pd.read_csv(lin(hour, i))
    a = a.append(b)

# merge dataframes
merged = a.append(b)
merged = merged.sort_values("id")

# write to csv
name = "./merged_files/" + str(hour) + "_" + str(hours) + "h.csv"
merged.to_csv(name, index=True)

print(merged.head(2000))
