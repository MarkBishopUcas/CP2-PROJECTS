import csv
import matplotlib.pyplot as plt
import pandas as pd

# Bar graph using Matplotlib for Win/Loss Ratio
def plot_wlr():
    characters = []
    win_loss_ratios = []

    # Read data from CSV
    with open("battle_simulator_upgrade/characters.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"].capitalize()
            wins = int(row["level"])
            losses = int(row["loss"])

            # Calculate WLR (adding 1 to avoid division by zero)
            wlr = (wins + 1) / (losses + 1)
            characters.append(name)
            win_loss_ratios.append(wlr)

    # Plot the bar graph
    plt.figure(figsize=(10, 5))
    plt.bar(characters, win_loss_ratios, color="skyblue")
    plt.xlabel("Character")
    plt.ylabel("Win/Loss Ratio")
    plt.title("Win/Loss Ratio of Characters")
    plt.xticks(rotation=45, ha="right")  # Rotate names for better readability
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Show the bar graph
    plt.show()

# Scatter plot using Matplotlib for speed vs. strength
def plot_speed_vs_strength():
    df = pd.read_csv("battle_simulator_upgrade/characters.csv")

    plt.figure(figsize=(8, 6))
    plt.scatter(df["speed"], df["strength"], color="green", alpha=0.6)
    plt.xlabel("Speed")
    plt.ylabel("Strength")
    plt.title("Speed vs Strength of Characters")
    plt.grid(True, linestyle="--", alpha=0.7)

    # Show the scatter plot
    plt.show()

# Function to calculate the correlation matrix using Pandas
def calculate_correlation():
    df = pd.read_csv("battle_simulator_upgrade/characters.csv")

    # Calculate correlation between the columns
    correlation = df[["speed", "strength", "defense", "critical_hit_%"]].corr()

    print("\nCorrelation between Attributes:")
    print(correlation)

# Function to display stats using Pandas (mean, median, mode, etc.)
def pdf():
    df = pd.read_csv("battle_simulator_upgrade/characters.csv")

    stats = {
        "speed": {
            "mean": df["speed"].mean(),
            "median": df["speed"].median(),
            "max": df["speed"].max(),
            "min": df["speed"].min()
        },
        "strength": {
            "mean": df["strength"].mean(),
            "median": df["strength"].median(),
            "max": df["strength"].max(),
            "min": df["strength"].min()
        },
        "defense": {
            "mean": df["defense"].mean(),
            "median": df["defense"].median(),
            "max": df["defense"].max(),
            "min": df["defense"].min()
        },
        "critical_hit_%": {
            "mean": df["critical_hit_%"].mean(),
            "median": df["critical_hit_%"].median(),
            "max": df["critical_hit_%"].max(),
            "min": df["critical_hit_%"].min()
        }
    }

    # Print the statistics
    for attribute, values in stats.items():
        print(f"\n{attribute.capitalize()} Stats:")
        for stat, value in values.items():
            print(f"  {stat.capitalize()}: {value}")

# Menu function for interacting with the data
def data_menu():
    while True:
        selection = input("(1) Win Loss Ratio Bar Graph\n(2) Mean, Median, Mode, and More\n(3) Speed vs Strength Scatter Plot\n(4) Correlation Matrix\n(5) Back to Main Menu\nPlease type the number corresponding to your selection: ")
        if selection == "1":
            plot_wlr()  # Bar graph for Win/Loss Ratio
        elif selection == "2":
            pdf()  # Stats (mean, median, etc.)
        elif selection == "3":
            plot_speed_vs_strength()  # Scatter plot for Speed vs Strength
        elif selection == "4":
            calculate_correlation()  # Correlation matrix
        elif selection == "5":
            return
        else:
            print("Please only select numbers 1-5")
