from time_handler import get_current_time, get_last_update_time
import datetime
import os

TIMESTAMP_FILE = "last_update.txt"

def file_select():
    file_path = input("Please copy and paste the path of your .txt file: ").strip()
    return file_path

def get_words_from_file(file_path):
    words = []
    try:
        with open(file_path, "r") as file:
            words.extend(file.read().split())
    except:
        print("Something went wrong, please try a different file path.")
    return words, get_last_update_time()

def write_word_count(word_count, timestamp):
    print(f"Word Count: {word_count} (Last Updated: {timestamp})")

def update_timestamp():
    with open(TIMESTAMP_FILE, "w") as file:
        file.write(get_current_time())

def edit_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        print("\nCurrent file content:\n")
        print(content)
        new_content = input("\nEnter your new content (this will overwrite the file):\n")
        with open(file_path, "w") as file:
            file.write(new_content)
        update_timestamp()
        print("File updated successfully!")
    except:
        print("Something went wrong while editing the file.")