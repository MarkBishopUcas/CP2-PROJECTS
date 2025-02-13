#initial commit with csv file attatched
import csv
titles = []
directors = []
genres = []
ratings = []
lengths = []
actors = []
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


"THIS FIX THIS "        
simplified_actors_converter = str(actors)
actors = simplified_actors_converter.split(",")
actors = actors.strip()
print(len(actors))
#search_term = input("Enter in the movie name, directors")
