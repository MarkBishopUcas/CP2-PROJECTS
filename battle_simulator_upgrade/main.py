import battle
import chatecter_creation
import battle_math

def main_menu():
    while True:
        choice = input("\n(1) TO BATTLE!\n(2) Character Creation\n(3) Data and Statistics\n(4) Exit\nPlease type the number corrosponding to your selection: ")
        if choice == "1":
            battle.pve_battle()
        elif choice == "2":
            chatecter_creation.character_creation_menu()
        elif choice == "3":
            battle_math.data_menu()
        elif choice == "4":
            print("Exiting game...")
            break
        else:
            print("Invalid selection, please choose again.")

if __name__ == "__main__":
    main_menu()
