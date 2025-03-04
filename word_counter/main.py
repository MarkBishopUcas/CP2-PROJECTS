from file_handler import file_select, get_words_from_file, write_word_count, edit_file
from time_handler import display_time

def main():
    file_path = None  # Ensure file_path is in scope
    while True:
        try:
            selection = int(input("\nWhere would you like to go?\n(1) Select File\n(2) Word Counter\n(3) Time Display\n(4) Edit File\n(5) Exit\nEnter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if selection == 1:
            file_path = file_select()
        elif selection == 2:
            if not file_path:
                print("No file selected. Please select a file first.")
                continue
            words = get_words_from_file(file_path)
            word_count = len(words)
            print(f"Word Count: {word_count}")
            write_word_count(file_path, word_count)
        elif selection == 3:
            display_time()
        elif selection == 4:
            if not file_path:
                print("No file selected. Please select a file first.")
                continue
            edit_file(file_path)
        elif selection == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()