# this is for myself so i can easily run it in the web browser version of vs code python3 /workspaces/CP2-PROJECTS/PersonalLibraryProgram/main.py

# these are all the lists used in all the functions
types = ()
names = ()
authors = ()
lengths = ()
genres = ()

#this function is for adding items to the library
def add_item_func(types, names, authors, lengths, genres):

    #converting tuple to list
    types = list(types)  
    names = list(names)  
    authors = list(authors)
    lengths = list(lengths)
    genres = list(genres) 

    #main part of function
    for i in range(int(input("How many items do you want to add to your library? "))):
        types.append(input(f"is item {i+1} a book, or a movie? ").lower())
        names.append(input(f"What is the name of your {types[i]}? ").lower())
        authors.append(input("What is the name of the author? ").lower())
        lengths.append(input(f"how long is the {types[i]}?(enter only as a number) "))
        genres.append(input(f"What genres does the {types[i]} fit into? (format: horror, fiction, historic, ect.) ").lower())
    
    #converting list back into tuple
    types = tuple(types)
    names = tuple(names)
    authors = tuple(authors)
    lengths = tuple(lengths)
    genres = tuple(genres)
    for i in range(len(names)):
            print(f"\n{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")

# Function for searching items in the library
def searcher_func(types, names, authors, lengths, genres):
    print("Search Options:")
    print("1. Search by type")
    print("2. Search by name")
    print("3. Search by author")
    print("4. Search by genre")
    
    search_choice = int(input("Enter the number corresponding to your choice: "))
    
    if search_choice == 1:
        search_type = input("Enter the type of item you want to search for (book/movie): ").lower()
        for i in range(len(names)):
            if types[i] == search_type:
                print(f"{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")
    
    elif search_choice == 2:
        search_name = input("Enter the name of the item you want to search for: ").lower()
        for i in range(len(names)):
            if search_name in names[i]:
                print(f"{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")
    
    elif search_choice == 3:
        search_author = input("Enter the author of the item you want to search for: ").lower()
        for i in range(len(names)):
            if search_author in authors[i]:
                print(f"{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")
    
    elif search_choice == 4:
        search_genre = input("Enter the genre of the item you want to search for: ").lower()
        for i in range(len(names)):
            if search_genre in genres[i]:
                print(f"{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")

    else:
        print("Invalid choice.")

# Function for modifying an item in the library
def modify_func(types, names, authors, lengths, genres):
    print("\nSelect the item number you want to modify:")
    for i in range(len(names)):
        print(f"{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")
    
    item_to_modify = int(input("\nEnter the number of the item you want to modify: ")) - 1
    
    if 0 <= item_to_modify < len(names):
        print(f"\nYou selected: {names[item_to_modify].title()} - {types[item_to_modify].title()} by {authors[item_to_modify].title()}")
        print("\nWhat would you like to modify?")
        print("1. Type")
        print("2. Name")
        print("3. Author")
        print("4. Length")
        print("5. Genre")
        
        modify_choice = int(input("Enter the number corresponding to the attribute you want to modify: "))
        
        if modify_choice == 1:
            types[item_to_modify] = input(f"Enter the new type for {names[item_to_modify]} (book/movie): ").lower()
        elif modify_choice == 2:
            names[item_to_modify] = input(f"Enter the new name for {names[item_to_modify]}: ").lower()
        elif modify_choice == 3:
            authors[item_to_modify] = input(f"Enter the new author for {names[item_to_modify]}: ").lower()
        elif modify_choice == 4:
            lengths[item_to_modify] = input(f"Enter the new length for {names[item_to_modify]}: ")
        elif modify_choice == 5:
            genres[item_to_modify] = input(f"Enter the new genre for {names[item_to_modify]}: ").lower()
        else:
            print("Invalid choice.")
        
        print(f"\nItem updated: {names[item_to_modify].title()} - {types[item_to_modify].title()} by {authors[item_to_modify].title()}, Length: {lengths[item_to_modify]}, Genres: {genres[item_to_modify].title()}")
    else:
        print("Invalid item number.")





#the code that displays the bookshelf in the main menu
def bookshelf_display_func(types):
    if len(names) <= 4:
        print(f"""
        Your Bookself
         |---------|
         |_________|
         |_________|
         |_________|
         |---------|
        """)
    elif len(names) <= 7:
        print(f"""
        Your Bookself
         |---------|
         ||x|_|x|__|
         |___|x|___|
         |_|x|__|x||
         |---------|
        """)
    elif len(names) >= 8:
        print(f"""
        Your Bookself
         |---------|
         ||X||X||X||
         ||X||X||X||
         ||X||X||X||
         |---------|
        """)


    

def main():
    list_made = 0
    while True:
        bookshelf_display_func(types)
        print("Where would you like to go? \n(1) Library Maker\n(2) Library Modifier\n(3) Library Searcher")
        lib_selection = int(input("\nEnter the number corresponding to your choice: "))
        if lib_selection == 1:
            add_item_func(types, names, authors, lengths, genres)
            list_made = 1
        elif lib_selection == 2:
            if list_made != 1: 
                print("You need to start a bookshelf before you can modify one. Go to Library Maker to start your library!")
            else:
                modify_func(types, names, authors, lengths, genres)
        elif lib_selection == 3:
            if list_made != 1: 
                print("You need to start a bookshelf before you can search. Go to Library Maker to start your library!")
            else:
                searcher_func(types, names, authors, lengths, genres)  # Call searcher function here
        if int(input("\nWould you like to continue to manage your library?\n\n1. Yes\n\n2. No\n\nEnter the number corresponding to your choice: ")) == 2:
            if int(input("\nAre you sure? You will lose all of your entered information.\n\n1. Yes\n\n2. No\n\nEnter the number corresponding to your choice: ")) == 1:
                print("Goodbye! Come again soon")
                break

#im not sure why we are supposed to do this, i read online you should run your main function like this because somtimes when importing your main function it can run? so this prevennts it acidentally running
if __name__ == "__main__":
    main()