import pandas as pd

hour = 18121401

a = pd.read_csv("files/"+ str(hour) + "/quotes.csv")
b = pd.read_csv("files/"+ str(hour+1) + "/quotes.csv")

merged = a.append(b)
merged.to_csv("merged.csv", index=False)

print("merged it")
##random change