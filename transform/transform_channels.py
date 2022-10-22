import traceback
from util import db_connection
import pandas as pd
import configparser


# Db stays the same
def tran_channels():
    try:
        # Connecting db
        conn = stg_conn.start()
        if conn == -1:
            raise Exception(f"The database type {stg_conn.type} is not valid")
        elif conn == -2:
            raise Exception("Error trying to connect to cdnastaging")

        # Dictionary of values

        colummns_dict = {
            "channel_id": [],
            "channel_desc": [],
            "channel_class": [],
            "channel_class_id": [],
        }

        # Read CSV
        channel_csv = pd.read_csv(config.get(cvsSectionName, "CHANNELS_PATH"))

        # Processing CSV content
        if not channel_csv.empty:
            for id, desc, ch_class, ch_class_id in zip(
                channel_csv["CHANNEL_ID"],
                channel_csv["CHANNEL_DESC"],
                channel_csv["CHANNEL_CLASS"],
                channel_csv["CHANNEL_CLASS_ID"],
            ):
                colummns_dict["channel_id"].append(id)
                colummns_dict["channel_desc"].append(desc)
                colummns_dict["channel_class"].append(ch_class)
                colummns_dict["channel_class_id"].append(ch_class_id)
        if colummns_dict["channel_id"]:
            conn.connect().execute("TRUNCATE TABLE channels_ext")
            # Creating Dataframe
            # Persisting into db
            df_channels = pd.DataFrame(colummns_dict)
            df_channels.to_sql("channels_ext", conn, if_exists="append", index=False)
            # Dispose db connection
            conn.dispose()
    except:
        traceback.print_exc()
    finally:
        pass
