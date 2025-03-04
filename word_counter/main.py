import file_handler

def main():
    try:
        selection = int(input("\nWhere would you like to go?\n(1) File select\n(2) Word counter\n(3) Time display\n(4) view/edit file\nType the number corrosponding to your selection: "))
    except:
        print("\nPlease only enter in a whole number")
        main()
    if selection == 1:
        file_handler.file_select()
    elif selection == 2:
        print("WIP")
main()