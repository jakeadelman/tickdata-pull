import pandas as pd


hour = 18121909
path = "merged_files/" + hour + "_4h_final.csv"

df = pd.read_csv(path)

the_range = len(df["id"])

for i in range(the_range):

    row = df.iloc[i, :]

    new_df = pd.DataFrame(columns=["id", "secondTime"])

