
#initial commit
#Create a to do list (Kept on a txt file). Add items to the to do list. Mark item as complete. Delete item from to do list
with open("to_do_list/to_do_list.txt", "r") as file:
    txt_reader = (file.read())
    print(txt_reader)