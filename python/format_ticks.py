import pandas as pd
import numpy as np
import sys


# set hour and get file location
hour = sys.argv[1]
hours = sys.argv[2]
loco = "files/" + str(hour) + "/ticks.csv"
write_loco = "files/" + str(hour) + "/formatted_ticks.csv"

# read file into df
df = pd.read_csv(loco)
# df = df.drop(columns=["timestamp", "symbol"])

df = df.sort_values(by=["id"])
df = df.drop(
    columns=[
        "volTime",
        "tickTime",
        "trdMatchID",
        "tickDirection",
        "side",
        "symbol",
        "hour",
        "id",
    ]
)
zeros = np.zeros(len(df["price"]), dtype=np.int)
data = {
    "Datetime": df["timestamp"],
    "Open": df["price"],
    "High": df["price"],
    "Low": df["price"],
    "Close": df["price"],
    "Volume": df["size"],
    "OpenInterest": zeros,
}

lengthy = len(df["price"]) + 1

a = np.arange(1, lengthy)
new_df = pd.DataFrame(data=data, index=np.array(a))

new_df.to_csv(write_loco, index=False)

print(new_df.head(20))

