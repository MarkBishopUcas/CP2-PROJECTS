import datetime
import os

TIMESTAMP_FILE = "last_update.txt"

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_last_update_time():
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, "r") as file:
            return file.read().strip()
    return "Unknown"

def display_time():
    current_time = get_current_time()
    last_timestamp = get_last_update_time()

    time_difference = "Unknown"
    if last_timestamp != "Unknown":
        try:
            last_time = datetime.datetime.strptime(last_timestamp, "%Y-%m-%d %H:%M:%S")
            current_dt = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
            time_difference = str(current_dt - last_time)
        except:
            pass

    print(f"Current Time: {current_time}")
    print(f"Time Since Last Update: {time_difference}")
