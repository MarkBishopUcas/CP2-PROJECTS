import random

def req_getter_func():
    length = int(input("How many charecters long does your password need to be? "))
    uppercase = 0
    number = 0
    spec_char = 0
    uppsers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    spec_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "|", ";", ":", ",", "\\", '"', "'",  "<", ".", ">", "/", "?", "`", "~", "}", "]"]
    password = []
    while uppercase > 3 or uppercase < 1:
        uppercase = int(input("\nDoes your password need to have uppercase letters?\n\n(1) No uppercase letters\n\n(2) Yes upercase letters\n\n(3) Only uppercase letters\n\nPlease type the number of your option: "))
        if uppercase > 3 or uppercase < 1:
            print("\nplease select only 1,2 or 3\n")
    while number > 2 or number < 1:
        number = int(input("\ndoes your password need to have number?\n\n(1) Yes\n\n(2) No\n\nPlease type the number of your option: "))
        if number > 2 or number < 1:
            print("\nplease select only 1 or 2\n")
    while spec_char > 2 or spec_char < 1:
        spec_char = int(input("\ndoes your password need to have special charecters?\n\n(1) Yes\n\n(2) No\n\nPlease type the number of your option: "))
        if spec_char > 2 or spec_char < 1:
            print("\nplease select only 1 or 2\n")
    for i in range(4):            
        for i in range(length):
            print("wip")
            

        



def main():
    req_getter_func()
if __name__ == "__main__":
    main()