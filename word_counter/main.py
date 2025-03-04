import file_handler
import time_handler

def main():
    file_path = None
    while True:
        try:
            selection = int(input("\nWhere would you like to go?\n(1) Select File\n(2) Word Counter\n(3) Time Display\n(4) Edit File\n(5) Exit\nEnter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if selection == 1:
            file_path = file_handler.file_select()
            words, last_timestamp = file_handler.get_words_from_file(file_path)
            word_count = len(words)
            print(f"Initial Word Count: {word_count}")
        elif selection == 2:
            if not file_path:
                print("No file selected. Please select a file first.")
                continue
            words, last_timestamp = file_handler.get_words_from_file(file_path)
            word_count = len(words)
            print(f"Word Count: {word_count}")
        elif selection == 3:
            time_handler.display_time()
        elif selection == 4:
            if not file_path:
                print("No file selected. Please select a file first.")
                continue
            file_handler.edit_file(file_path)
        elif selection == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()

