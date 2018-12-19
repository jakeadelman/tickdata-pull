import pandas as pd


## manually set hour
hour = 18121405

## read 4 csv files and concat into one
a = pd.read_csv("files/" + str(hour) + "/quotes.csv")
b = pd.read_csv("files/" + str(hour + 1) + "/quotes.csv")
c = pd.read_csv("files/" + str(hour + 2) + "/quotes.csv")
d = pd.read_csv("files/" + str(hour + 3) + "/quotes.csv")

## merge dataframes
merged = a.append(b)
merged = merged.append(c)
merged = merged.append(d)

## write to csv
name = "./merged_files/" + str(hour) + "_4h.csv"
merged.to_csv(name, index=True)

print("merged it")
