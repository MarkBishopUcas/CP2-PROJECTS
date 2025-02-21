
#initial commit
#Create a to do list (Kept on a txt file). Add items to the to do list. Mark item as complete. Delete item from to do list
dict_todo = {}
with open("to_do_list/to_do_list.txt", "r") as file:
    txt_reader = (file.read())
    lst_todo = txt_reader.split(",")

    for i in range(2,len(lst_todo),2):
        dict_todo.update({lst_todo[i]: lst_todo[i+1]})
    print(dict_todo)

def add_item():
    print("wip")

def modify_item():
    print("wip")

def complete():
    print("wip")

def main():
    print("wip")
