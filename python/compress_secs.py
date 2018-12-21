import pandas as pd
import numpy as np
import sys

# set hour and get file location
hour = sys.argv[1]
hours = sys.argv[2]
loco = "merged_files/" + str(hour) + "_" + str(hours) + "h.csv"

# read file into df
df = pd.read_csv(loco)
df = df.drop(columns=["timestamp", "symbol"])

# compress to seconds function
def compress(df):

    # create final dataframe
    final_df = pd.DataFrame(
        columns=["id", "secondTime", "microOpen", "microClose", "midOpen", "midClose"]
    )

    # set val to zero and get num rows
    val = 0
    other_count = 0
    the_range = len(df["id"])

    # iterate through rows
    for i in range(the_range):

        # get row
        row = df.iloc[i, :]

        # create variable dict -- changes every row iteration
        variables = {}
        variables = {}
        # "id": null,
        # "secondTime": null,
        # "microOpen": null,
        # "microClose": null,
        # "midOpen": null,
        # "midClose": null,

        # get the second from row
        sec = row["secondTime"]
        print(sec, "SECOND TIME", i)

        # if second not added -- add row to final df
        if len(final_df) == 0 or sec != val:

            val = sec
            other_count += 1

            # take average microPrice
            locco_micro_p = df.loc[df["secondTime"] == sec, "microPrice"]
            locco_micro_p = np.array(locco_micro_p)
            # locco_micro_p = sum(locco_micro_p[:]) / len(locco_micro_p)
            micro_open = locco_micro_p[0]
            micro_close = locco_micro_p[-1]

            # take average midPrice
            locco_mid_p = df.loc[df["secondTime"] == sec, "midPrice"]
            locco_mid_p = np.array(locco_mid_p)
            # locco_mid_p = sum(locco_mid_p[:]) / len(locco_mid_p)
            mid_open = locco_mid_p[0]
            mid_close = locco_mid_p[-1]

            variables["id"] = other_count
            variables["secondTime"] = sec
            variables["microOpen"] = micro_open
            variables["microClose"] = micro_close
            variables["midOpen"] = mid_open
            variables["midClose"] = mid_close

            final_df = final_df.append(variables, ignore_index=True)

        # if second exists in final dataframe
        # if sec == val:

        # # take average bidPrice
        # locco_bid_p = df.loc[df["secondTime"] == sec, "bidPrice"]
        # locco_bid_p = np.array(locco_bid_p)
        # locco_bid_p = sum(locco_bid_p[:]) / len(locco_bid_p)

        # # take average bidSize
        # locco_bid_s = df.loc[df["secondTime"] == sec, "bidSize"]
        # locco_bid_s = np.array(locco_bid_s)
        # locco_bid_s = sum(locco_bid_s[:]) / len(locco_bid_s)

        # # take average askPrice
        # locco_ask_p = df.loc[df["secondTime"] == sec, "askPrice"]
        # locco_ask_p = np.array(locco_ask_p)
        # locco_ask_p = sum(locco_ask_p[:]) / len(locco_ask_p)

        # # take average askSize
        # locco_ask_s = df.loc[df["secondTime"] == sec, "askSize"]
        # locco_ask_s = np.array(locco_ask_s)
        # locco_ask_s = sum(locco_ask_s[:]) / len(locco_ask_s)

        # # take average microPrice
        # locco_micro_p = df.loc[df["secondTime"] == sec, "microPrice"]
        # locco_micro_p = np.array(locco_micro_p)
        # # locco_micro_p = sum(locco_micro_p[:]) / len(locco_micro_p)
        # micro_open = locco_micro_p[0]
        # micro_close = locco_micro_p[-1]

        # # take average midPrice
        # locco_mid_p = df.loc[df["secondTime"] == sec, "midPrice"]
        # locco_mid_p = np.array(locco_mid_p)
        # # locco_mid_p = sum(locco_mid_p[:]) / len(locco_mid_p)
        # mid_open = locco_mid_p[0]
        # mid_close = locco_mid_p[-1]

        # # take last row of final df and replace temp df with vals
        # temp_val = final_df.iloc[-1, :]
        # temp_val["id"] = other_count
        # temp_val["bidPrice"] = round(locco_bid_p, 3)
        # temp_val["bidSize"] = round(locco_bid_s, 3)
        # temp_val["askPrice"] = round(locco_ask_p, 3)
        # temp_val["askSize"] = round(locco_ask_s, 3)

        # # replace last row of final df with avg values
        # final_df.iloc[-1, :] = temp_val

    # write final df to csv
    # final_df = final_df.drop(columns=["id"])
    loco_update = "merged_files/" + str(hour) + "_4h_final.csv"
    final_df.to_csv(loco_update)


# run function
compress(df)
