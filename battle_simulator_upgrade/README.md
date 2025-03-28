# Battle Simulator

## Project Description

Battle Simulator is a turn-based combat game where players choose a character and engage in battles against CPU-controlled opponents. The game features:
- Character customization
- Randomized attacks with critical hits and dodge mechanics
- Power attacks and healing options
- A character leveling system
- Statistical analysis of battle data

## Execution and Usage
---
- **TO BATTLE!** - Engage in a fight against the CPU.
- **Character Creation** - Create and customize new characters.
- **Data Analysis** - View statistical information about characters, including win/loss ratios, attributes, and correlations.

## Installation Instructions
---
1. Install Python (if not already installed).
2. Install required dependencies using:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the game by executing:
   ```sh
   python main.py
   ```

## Used Technologies
---
- **Python** - Core language for game logic.
- **CSV Module** - Stores and retrieves character data.
  ```python
  import csv
  ```
- **Random Module** - Handles randomized attack outcomes.
  ```python
  import random
  ```
- **Faker Module** - Generates random backstories and character names.
  ```python
  import faker
  ```
- **Matplotlib** - Visualizes data such as win/loss ratios and attributes through bar graphs and scatter plots.
  ```python
  import matplotlib
  ```
- **Pandas** - Analyzes character data and generates statistical summaries and correlation matrices.
  ```python
  import pandas
  ```

## Current Features
---
- Character selection with unique stats.
- Turn-based combat system with strategic attack choices.
- Randomized critical hits and dodge mechanics.
- Power attacks and healing options.
- Character leveling system that affects stats and battle outcomes.
- Statistical analysis of character performance using data visualization.

## Author's Info
---
I am Mark Bishop, a developer interested in game development and coding challenges.

## Change Log
---
- None yet.
