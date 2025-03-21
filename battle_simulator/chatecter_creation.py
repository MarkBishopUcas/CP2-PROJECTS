import csv

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
                print("please only enter numbers 1-3")
        except ValueError:
            print("\nPlease only enter whole numbers")

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
                print("please only enter numbers 1-3")
        except ValueError:
            print("\nPlease only enter whole numbers")

def allocate_skill_points(stats):
    i = 25
    while i > 0:
        print(f"\nyou have {i} points to put into the skill pool")
        try:
            pool = int(input(f"please select the skill you want your point to go into\n(1) Speed {stats['speed']}\n(2) Strength {stats['strength']}\n(3) Defense {stats['defense']}\n(4) Critical hit chance {stats['critical_hit_%']}\nPlease type the number corresponding to your selection: "))
            if pool == 1:
                stats["speed"] += 1
            elif pool == 2:
                stats["strength"] += 1
            elif pool == 3:
                stats["defense"] += 1
            elif pool == 4:
                stats["critical_hit_%"] += 1
            else:
                print("please only enter numbers 1-4")
                i += 1
        except ValueError:
            print("Please only enter whole numbers.")
            i += 1
        i -= 1

def create_char():
    stats = {"speed": 10, "strength": 10, "defense": 10, "critical_hit_%": 5}
    data = []
    name = input("Please enter the name of your new character: ").lower().strip()
    char_class = get_class_choice(stats)
    attribute = get_attribute_choice(stats)
    allocate_skill_points(stats)
    
    new_char = {
        "name": name,
        "class": char_class,
        "attribute": attribute,
        "speed": stats["speed"],
        "strength": stats["strength"],
        "defense": stats["defense"],
        "critical_hit_%": stats["critical_hit_%"],
        "level": 0
    }
    data.append(new_char)
    save_char_csv(data)

def save_char_csv(data):
    with open("battle_simulator/characters.csv", "a+", newline="") as file:
        fieldnames = ["name", "class", "attribute", "speed", "strength", "defense", "critical_hit_%", "level"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerows(data)

def level_up_character(name):
    characters = []
    name = name.lower().strip()
    with open("battle_simulator/characters.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] == name:
                row["level"] = str(int(row["level"]) + 1)
            characters.append(row)
    with open("battle_simulator/characters.csv", "w", newline="") as file:
        fieldnames = ["name", "class", "attribute", "speed", "strength", "defense", "critical_hit_%", "level"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)

#create_char()