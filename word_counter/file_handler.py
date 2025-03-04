from time_handler import get_current_time

def file_select():
    file_input = input("Please copy and paste the path of your .txt file: ").strip()
    
    return file_input

def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            word_list = content.split()  # Splits by any whitespace
            return word_list
    except:
        print("Something went wrong, please try a different file path.")
        return []

def write_word_count(file_path, word_count):
    try:
        timestamp = get_current_time()
        with open(file_path, "a") as file:  # Append mode
            file.write(f"\nWord Count: {word_count}\nLast Updated: {timestamp}\n")
        print("Word count updated successfully!")
    except:
        print("Something went wrong, please try a different file path.")

def edit_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print("\nCurrent file content:\n")
            print(content)
        
        new_content = input("\nEnter your new content (this will overwrite the file):\n")
        
        with open(file_path, "w") as file:
            file.write(new_content)
        
        # Update the timestamp after editing
        timestamp = get_current_time()
        with open(file_path, "a") as file:
            file.write(f"\nLast Updated: {timestamp}\n")
        
        print("File updated successfully!")
    except:
        print("Something went wrong, please try a different file path.")