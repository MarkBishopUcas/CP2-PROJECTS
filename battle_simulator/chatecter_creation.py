import csv

data = [{"name": "Josh", "class": "Warior", "attribute": "tank", "speed": "8", "strength": "20", "defense": "60", "magic": "0", "mana": "0", "critical_hit_%": "6"}]

def save_char_csv():
    print("WIP")
    with open("battle_simulator/charecters.csv", "a+", newline="") as file:
        csv_reader = csv.reader(file)
        feildnames = ["name", "class", "attribute", "speed", "strength", "defense", "magic", "mana", "critical_hit_%"]
        writer = csv.DictWriter(file,fieldnames=feildnames)
        writer.writerows(data)
        
save_char_csv()