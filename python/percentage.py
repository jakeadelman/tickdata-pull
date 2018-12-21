import pandas as pd
import sys

# Set variables
hour = sys.argv[1]
hours = sys.argv[2]

print(args)

path = "merged_files/" + str(hour) + "_" + str(hours) + "h_final.csv"
new_path = "merged_files/" + str(hour) + "_" + str(hours) + "h_perc.csv"

# Read df
df = pd.read_csv(path)


def percentage_gain(df, new_path):

    new_path = new_path
    the_range = len(df["id"])
    print("the range is :: ", the_range)

    new_df = pd.DataFrame(
        columns=[
            "id",
            "secondTime",
            "midOpen",
            "midClose",
            "microOpen",
            "microClose",
            "returnsOpenPrevMid1",
            "returnsClosePrevMid1",
            "returnsOpenPrevMicro1",
            "returnsClosePrevMicro1",
            "returnsOpenPrevMid10",
            "returnsClosePrevMid10",
            "returnsOpenPrevMicro10",
            "returnsClosePrevMicro10",
        ]
    )

    count = 0

    for i in range(the_range):

        row = df.iloc[i, :]
        variables = {}

        if count == 0:
            variables["id"] = row["id"]
            variables["secondTime"] = row["secondTime"]
            variables["midOpen"] = row["midOpen"]
            variables["midClose"] = row["midClose"]
            variables["microOpen"] = row["microOpen"]
            variables["microClose"] = row["microClose"]
            variables["returnsOpenPrevMid1"] = 0
            variables["returnsClosePrevMid1"] = 0
            variables["returnsOpenPrevMicro1"] = 0
            variables["returnsClosePrevMicro1"] = 0
            variables["returnsOpenPrevMid10"] = 0
            variables["returnsClosePrevMid10"] = 0
            variables["returnsOpenPrevMicro10"] = 0
            variables["returnsClosePrevMicro10"] = 0

            new_df = new_df.append(variables, ignore_index=True)
            print(new_df)
            count += 1

        if count > 0 and count < 10:

            last_row = new_df.iloc[-1, :]
            ret_open_mid_1 = (row["midOpen"] - last_row["midOpen"]) / last_row[
                "midOpen"
            ]
            ret_close_mid_1 = (row["midClose"] - last_row["midClose"]) / last_row[
                "midClose"
            ]
            ret_open_micro_1 = (row["microOpen"] - last_row["microOpen"]) / last_row[
                "microOpen"
            ]
            ret_close_micro_1 = (row["microClose"] - last_row["microClose"]) / last_row[
                "microClose"
            ]

            variables["id"] = row["id"]
            variables["secondTime"] = row["secondTime"]
            variables["midOpen"] = row["midOpen"]
            variables["midClose"] = row["midClose"]
            variables["microOpen"] = row["microOpen"]
            variables["microClose"] = row["microClose"]
            variables["returnsOpenPrevMid1"] = ret_open_mid_1
            variables["returnsClosePrevMid1"] = ret_close_mid_1
            variables["returnsOpenPrevMicro1"] = ret_open_micro_1
            variables["returnsClosePrevMicro1"] = ret_close_micro_1
            variables["returnsOpenPrevMid10"] = 0
            variables["returnsClosePrevMid10"] = 0
            variables["returnsOpenPrevMicro10"] = 0
            variables["returnsClosePrevMicro10"] = 0

            new_df = new_df.append(variables, ignore_index=True)
            print(new_df)
            count += 1

        if count >= 10:
            last_row = new_df.iloc[-1, :]
            ten_ago = new_df.iloc[-10, :]

            ret_open_mid_1 = (row["midOpen"] - last_row["midOpen"]) / last_row[
                "midOpen"
            ]
            ret_close_mid_1 = (row["midClose"] - last_row["midClose"]) / last_row[
                "midClose"
            ]
            ret_open_micro_1 = (row["microOpen"] - last_row["microOpen"]) / last_row[
                "microOpen"
            ]
            ret_close_micro_1 = (row["microClose"] - last_row["microClose"]) / last_row[
                "microClose"
            ]

            ret_open_mid_10 = (row["midOpen"] - ten_ago["midOpen"]) / ten_ago["midOpen"]
            ret_close_mid_10 = (row["midClose"] - ten_ago["midClose"]) / ten_ago[
                "midClose"
            ]
            ret_open_micro_10 = (row["microOpen"] - ten_ago["microOpen"]) / ten_ago[
                "microOpen"
            ]
            ret_close_micro_10 = (row["microClose"] - last_row["microClose"]) / ten_ago[
                "microClose"
            ]

            variables["id"] = row["id"]
            variables["secondTime"] = row["secondTime"]
            variables["midOpen"] = row["midOpen"]
            variables["midClose"] = row["midClose"]
            variables["microOpen"] = row["microOpen"]
            variables["microClose"] = row["microClose"]
            variables["returnsOpenPrevMid1"] = ret_open_mid_1
            variables["returnsClosePrevMid1"] = ret_close_mid_1
            variables["returnsOpenPrevMicro1"] = ret_open_micro_1
            variables["returnsClosePrevMicro1"] = ret_close_micro_1
            variables["returnsOpenPrevMid10"] = ret_open_mid_10
            variables["returnsClosePrevMid10"] = ret_close_mid_10
            variables["returnsOpenPrevMicro10"] = ret_open_micro_10
            variables["returnsClosePrevMicro10"] = ret_close_micro_10

            new_df = new_df.append(variables, ignore_index=True)
            print(new_df)
            count += 1

    new_df.to_csv(new_path, float_format="%.6f")
    print("done")


percentage_gain(df, new_path)
