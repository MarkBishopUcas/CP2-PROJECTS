#initial commit with csv file attatched
import csv
titles = []
directors = []
genres = []
ratings = []
lengths = []
actors = []
place = []
with open("MovieRecommender/movies_list.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        #print(f"\n\nTitle {row[0]},\nDirector {row[1]},\nGenre {row[2]},\nRating {row[3]},\nLength (min) {row[4]},\nNotable Actors {row[5]}.")
        titles.append(row[0])
        directors.append(row[1])
        genres.append(row[2])
        ratings.append(row[3])
        lengths.append(row[4])
        actors.append(row[5])

search_term = input("Which actors are you looking for? ").title()
for i in range(len(actors)):
    if search_term in actors[i]:
        print("True")
        place.append(i)
    else:
        print("False")
for i in range(len(place)):
    print(f"\n\nTitle {titles[place[i]]},\nDirector {directors[place[i]]},\nGenre {genres[place[i]]},\nRating {ratings[place[i]]},\nLength (min) {lengths[place[i]]},\nNotable Actors {actors[place[i]]}.")

def search_func():
    while True:
        try:
            selection = int(input("Would you like to search for a movie, or filter for one?\n\n(1) Search\n(2) Filter"))
            if selection == 1:
                print("WIP")
            elif selection == 2:
                while True:
                    try:
                        selection = int(input("What would you like to filter for?\n\n(1) Movie Titles\n(2) Movie directors\n(3) Movie genres\n(4) Movie ratings\n(5) Movie durration\n(6) Notable actors"))
                        if selection == 1:
                            print("WIP")
                        elif selection == 2:
                            print("WIP")
                        elif selection == 3:
                            print("WIP")
                        elif selection == 4:
                            print("WIP")
                        elif selection == 5:
                            print("WIP")
                        elif selection == 6:
                            print("WIP")
                        else:
                            print("Please only enter numbers 1-6.")
                    except:
                        print("Please only enter in a whole number.")
                    

            else:
                print("Please only type 1, or 2.")
        except:
            print("please only enter in a whole number.")
            

def main():
    print("WIP")

