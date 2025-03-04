import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def display_time():
    print(f"Current Time: {get_current_time()}")
