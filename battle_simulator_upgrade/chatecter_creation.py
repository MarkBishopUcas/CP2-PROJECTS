import csv
from faker import Faker

fake = Faker()

# Function to create and save a new character
import csv
from faker import Faker
fake = Faker()

#the main function that contains functions necessary for character creation
def create_char():
    def get_class_choice(stats):
        while True:
            try:
                char_class = int(input("\nPlease select your class\n(1) Warrior: +10 strength, +10 defense\n(2) Monk: +10 speed, +5% critical hit chance\n(3) Tank: +20 defense, +5 strength\nPlease type the number corresponding to your selection: "))
                if char_class == 1:
                    stats["strength"] += 10
                    stats["defense"] += 10
                    return "warrior"
                elif char_class == 2:
                    stats["speed"] += 10
                    stats["critical_hit_%"] += 5
                    return "monk"
                elif char_class == 3:
                    stats["defense"] += 20
                    stats["strength"] += 5
                    return "tank"
                else:
                    print("Please only enter numbers 1-3.")
            except ValueError:
                print("\nPlease only enter whole numbers.")

    def get_attribute_choice(stats):
        while True:
            try:
                attribute = int(input("\nPlease select your attribute\n(1) Speedster: +15 speed\n(2) Lucky +15% critical hit chance\n(3) Brawler +10 strength\nPlease type the number corresponding to your selection: "))
                if attribute == 1:
                    stats["speed"] += 15
                    return "speedster"
                elif attribute == 2:
                    stats["critical_hit_%"] += 15
                    return "lucky"
                elif attribute == 3:
                    stats["strength"] += 10
                    return "brawler"
                else:
                    print("Please only enter numbers 1-3.")
            except ValueError:
                print("\nPlease only enter whole numbers.")

    def allocate_skill_points(stats):
        i = 25
        while i > 0:
            print(f"\nYou have {i} points to allocate.")
            try:
                pool = int(input(f"Please select the skill you want your point to go into\n(1) Speed {stats["speed"]}\n(2) Strength {stats["strength"]}\n(3) Defense {stats["defense"]}\n(4) Critical hit chance {stats["critical_hit_%"]}\nPlease type the number corresponding to your selection: "))
                if pool == 1:
                    stats["speed"] += 1
                elif pool == 2:
                    stats["strength"] += 1
                elif pool == 3:
                    stats["defense"] += 1
                elif pool == 4:
                    stats["critical_hit_%"] += 1
                else:
                    print("Please only enter numbers 1-4.")
                    i += 1
            except ValueError:
                print("Please only enter whole numbers.")
                i += 1
            i -= 1

    # Base stats before modifiers
    stats = {"speed": 10, "strength": 10, "defense": 10, "critical_hit_%": 5}
    data = []
    name = input("\nPlease enter the name of your new character, or input 'random' for a random name: ").lower().strip()
    if name == "random":
        name = fake.name()
    
    # Generate backstory randomly or allow user input
    backstory = input("\nPlease enter your backstory, or type 'random' for a random backstory: ").lower()
    if backstory == "random":
        backstory = fake.text(max_nb_chars=200)

    county = input("\nPlease enter your country, or type 'random' for a random country: ").lower()
    if county == "random":
        county = fake.county()

    char_class = get_class_choice(stats)
    attribute = get_attribute_choice(stats)
    allocate_skill_points(stats)

    # Setting up the dictionary that needs to be inside the list data to be added to the CSV
    name = name.lower().strip()
    new_char = {
        "name": name,
        "class": char_class,
        "attribute": attribute,
        "speed": stats["speed"],
        "strength": stats["strength"],
        "defense": stats["defense"],
        "critical_hit_%": stats["critical_hit_%"],
        "level": 0,
        "loss": 0,
        "backstory": backstory,
        "country": county
    }
    data.append(new_char)
    save_char_csv(data)

def save_char_csv(data):
    with open("battle_simulator_upgrade/characters.csv", "a+", newline="") as file:
        fieldnames = ["name", "class", "attribute", "speed", "strength", "defense", "critical_hit_%", "level", "loss", "backstory", "country"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerows(data)


# Function to view all characters
def view_all_characters():
    with open("battle_simulator_upgrade/characters.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            #used for debugging 
            #print(row)
            #print(row.keys())
            print(f"\nName: {row["name"]}")
            print(f"Class: {row["class"]}")
            print(f"Attribute: {row["attribute"]}")
            print(f"Speed: {row["speed"]}")
            print(f"Strength: {row["strength"]}")
            print(f"Defense: {row["defense"]}")
            print(f"Critical Hit Chance: {row["critical_hit_%"]}")
            print(f"Level: {row["level"]}")
            print(f"Losses: {row["loss"]}")
            print(f"Backstory: {row["backstory"]}")
            print(f"Country that {row["name"]} is representing: {row["country"]}.")

# Function to level up character
def level_up_character(name):
    characters = []
    name = name.lower().strip()
    with open("battle_simulator_upgrade/characters.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] == name:
                row["level"] = str(int(row["level"]) + 1)
            characters.append(row)
    with open("battle_simulator_upgrade/characters.csv", "w", newline="") as file:
        fieldnames = ["name", "class", "attribute", "speed", "strength", "defense", "critical_hit_%", "level", "loss", "backstory", "country"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)

# Record character loss
def record_loss(name):
    characters = []
    name = name.lower().strip()
    with open("battle_simulator_upgrade/characters.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] == name:
                row["loss"] = str(int(row["loss"]) + 1)
            characters.append(row)
    with open("battle_simulator_upgrade/characters.csv", "w", newline="") as file:
        fieldnames = ["name", "class", "attribute", "speed", "strength", "defense", "critical_hit_%", "level", "loss", "backstory", "country"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)

# Function to display character creation menu and view all characters
def character_creation_menu():
    while True:
        choice = input("\nCharacter Creation Menu:\n(1) Create a new character\n(2) View all characters\n(3) Back to main menu\nPlease select an option: ")
        if choice == "1":
            create_char()
        elif choice == "2":
            view_all_characters()
        elif choice == "3":
            return
        else:
            print("Invalid choice, please select again.")

#character_creation_menu()
