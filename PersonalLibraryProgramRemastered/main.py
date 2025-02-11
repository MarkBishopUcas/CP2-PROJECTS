# Function for adding items to the library
def add_item_func(library):
    for i in range(int(input("How many items do you want to add to your library? "))):
        book = {}

        book["type"] = input(f"Is item {i+1} a book, or a movie? ").strip().lower()
        book["name"] = input(f"What is the name of your {book["type"]}? ").strip().lower()
        book["author"] = input("What is the name of the author? ").strip().lower()
        book["length"] = input(f"How long is the {book["type"]}? (enter only as a number) ").strip()
        book["genre"] = input(f"What genres does the {book["type"]} fit into? (format: horror, fiction, historic, etc.) ").strip().lower()

        library = list(library)
        library.append(book)
        library = tuple(library)
    
    for i, book in enumerate(library, start=1):
        print(f"\n{i}. {book["name"].title()} - {book["type"].title()} by {book["author"].title()}, Length: {book["length"]}, Genres: {book["genre"].title()}")

    return library

# Function for searching items in the library
def searcher_func(library):
    for i, book in enumerate(library, start=1):
        print(f"\n{i}. {book["name"].title()} - {book["type"].title()} by {book["author"].title()}, Length: {book["length"]}, Genres: {book["genre"].title()}")

    search_term = input("Enter the name of the item you are searching for: ").strip().lower()
    found = False

    for i, book in enumerate(library, start=1):
        if search_term in book["name"]:
            print(f"\n{i}. {book["name"].title()} - {book["type"].title()} by {book["author"].title()}, Length: {book["length"]}, Genres: {book["genre"].title()}")
            found = True

    if not found:
        print("\nNo items found with that name.")

# Function for modifying an item in the library
def modify_func(library):
    library = list(library)
    
    for i, book in enumerate(library, start=1):
        print(f"\n{i}. {book["name"].title()} - {book["type"].title()} by {book["author"].title()}, Length: {book["length"]}, Genres: {book["genre"].title()}")

    search_term = input("Enter the name of the item you want to modify: ").strip().lower()
    found_indexes = []

    for i, book in enumerate(library):
        if search_term in book["name"]:
            print(f"\n{i+1}. {book["name"].title()} - {book["type"].title()} by {book["author"].title()}, Length: {book["length"]}, Genres: {book["genre"].title()}")
            found_indexes.append(i)

    if not found_indexes:
        print("\nNo items found with that name.")
        return tuple(library)

    if len(found_indexes) > 1:
        selection = int(input("\nMultiple matches found. Enter the number corresponding to the item you want to modify: ")) - 1
    else:
        selection = found_indexes[0]

    while True:
        print("\nWhat would you like to modify?")
        print("1. Name\n2. Type\n3. Author\n4. Length\n5. Genres\n6. Go back to main menu")
        choice = input("Enter the number corresponding to your choice: ").strip()

        if choice == "1":
            library[selection]["name"] = input("Enter the new name: ").strip().lower()
        elif choice == "2":
            library[selection]["type"] = input("Enter the new type (book/movie): ").strip().lower()
        elif choice == "3":
            library[selection]["author"] = input("Enter the new author: ").strip().lower()
        elif choice == "4":
            library[selection]["length"] = input("Enter the new length: ").strip()
        elif choice == "5":
            library[selection]["genre"] = input("Enter the new genres (format: horror, fiction, etc.): ").strip().lower()
        elif choice == "6":
            print("\nReturning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

        print("\nItem modified successfully!")
        print(f"\n{selection+1}. {library[selection]["name"].title()} - {library[selection]["type"].title()} by {library[selection]["author"].title()}, Length: {library[selection]["length"]}, Genres: {library[selection]["genre"].title()}")

    return tuple(library)

# Function for viewing the library
def viewer_func(library):
    if not library:
        print("Your library is empty! Add some items first.")
        return

    for i, book in enumerate(library, start=1):
        print(f"\n{i}. {book["name"].title()} - {book["type"].title()} by {book["author"].title()}, Length: {book["length"]}, Genres: {book["genre"].title()}")

# Main function
def main():
    library = ()

    while True:
        try:
            print("\nWhere would you like to go?")
            print("(1) Library Maker\n(2) Library Modifier\n(3) Library Searcher\n(4) Library Viewer")

            lib_selection = int(input("\nEnter the number corresponding to your choice: "))

            if lib_selection == 1:
                library = add_item_func(library)
            elif lib_selection == 2:
                if not library:
                    print("You need to start a bookshelf before you can modify it. Go to Library Maker to start your library!")
                else:
                    library = modify_func(library)
            elif lib_selection == 3:
                if not library:
                    print("You need to start a bookshelf before you can search it. Go to Library Maker to start your library!")
                else:
                    searcher_func(library)
            elif lib_selection == 4:
                viewer_func(library)
            else:
                print("\nPlease only enter numbers 1-4.")

            if int(input("\nWould you like to continue to manage your library?\n\n1. Yes\n\n2. No\n\nEnter the number corresponding to your choice: ")) == 2:
                print("Goodbye! Come again soon.")
                break
        except ValueError:
            print("\nPlease only enter a whole number.")

if __name__ == "__main__":
    main()
