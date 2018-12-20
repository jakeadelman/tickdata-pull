import pandas as pd


# manually set hour
hour = 18121909

# read 4 csv files and concat into one
a = pd.read_csv("files/" + str(hour) + "/quotes.csv")
b = pd.read_csv("files/" + str(hour + 1) + "/quotes.csv")

# merge dataframes
merged = a.append(b)
merged = merged.sort_values("id")

# write to csv
name = "./merged_files/" + str(hour) + "_4h.csv"
merged.to_csv(name, index=True)

print(merged.head(2000))
