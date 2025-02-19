# Movie Recommender

import csv

# Lists to store movie data
titles = []
directors = []
genres = []
ratings = []
lengths = []
actors = []
place = []

# Dictionary to store filter options
filters = {
    "rating": "0",  # Default to no rating filter
    "length": None    # Default to no length filter
}

# Load movie data from CSV file
with open("MovieRecommender/movies_list.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        titles.append(row[0])
        directors.append(row[1])
        genres.append(row[2])
        ratings.append(row[3])
        lengths.append(int(row[4]) if row[4].isdigit() else 0)  # Convert length to int, default to 0 if empty
        actors.append(row[5])

# Function to search for movies based on user input
def search_movies():
    while True:
        search_term = input("Enter a movie title, director, genre, rating, length, actor, or type 1 to return to the main menu: ")

        if search_term == "1":
            return  # Return to main menu

        place.clear()  # Clear previous search results

        # Check each movie to see if it matches the search term and applied filters
        for i in range(len(titles)):
            if any(search_term.lower() in item.lower() for item in (titles[i], directors[i], genres[i], ratings[i], str(lengths[i]), actors[i])):
                rating_match = filters["rating"] == "0" or filters["rating"] == ratings[i] or ratings[i] in ["", "Unrated"]
                length_match = filters["length"] is None or (lengths[i] >= filters["length"] - 15 and lengths[i] <= filters["length"] + 15)

                if rating_match and length_match:
                    place.append(i)

        # Display search results
        if place:
            for i in place:
                print(f"\nTitle: {titles[i]}\nDirector: {directors[i]}\nGenre: {genres[i]}\nRating: {ratings[i] if ratings[i] else 'Unrated'}\nLength (min): {lengths[i]}\nNotable Actors: {actors[i]}")
        else:
            print("\nNo movies matched your search. Try adjusting your filters or searching with a different term!")

# Function to apply filters to movie searches
def apply_filters():
    while True:
        try:
            selection = int(input("\nFilter Options:\n(1) Apply a rating filter\n(2) Apply a movie duration filter\n(3) Return to main menu\nEnter your choice: "))

            if selection == 1:
                while True:
                    try:
                        # Display current rating filter selection
                        if filters["rating"] == "G":
                            print("\n(X) G\n(2) PG\n(3) PG-13\n(4) R\n(5) No rating filter\n(6) Other filtering options\n*Note: Unrated movies are always displayed.")
                        elif filters["rating"] == "PG":
                            print("\n(1) G\n(X) PG\n(3) PG-13\n(4) R\n(5) No rating filter\n(6) Other filtering options\n*Note: Unrated movies are always displayed.")
                        elif filters["rating"] == "PG-13":
                            print("\n(1) G\n(2) PG\n(X) PG-13\n(4) R\n(5) No rating filter\n(6) Other filtering options\n*Note: Unrated movies are always displayed.")
                        elif filters["rating"] == "R":
                            print("\n(1) G\n(2) PG\n(3) PG-13\n(X) R\n(5) No rating filter\n(6) Other filtering options\n*Note: Unrated movies are always displayed.")
                        elif filters["rating"] == "0":
                            print("\n(1) G\n(2) PG\n(3) PG-13\n(4) R\n(X) No rating filter\n(6) Other filtering options\n*Note: Unrated movies are always displayed.")
                        else:
                            print("\n(1) G\n(2) PG\n(3) PG-13\n(4) R\n(5) No rating filter\n(6) Other filtering options\n*Note: Unrated movies are always displayed.")

                        rating = int(input("\nSelect a rating filter: "))

                        if rating == 1:
                            rating = "G"
                        elif rating == 2:
                            rating = "PG"
                        elif rating == 3:
                            rating = "PG-13"
                        elif rating == 4:
                            rating = "R"
                        elif rating == 5:
                            rating = "0"
                        elif rating == 6:
                            break
                        else:
                            print("\nPlease enter a number between 1-6.")
                            continue

                        filters["rating"] = rating  # Update rating filter
                    except:
                        print("\nPlease enter a valid number.")
            elif selection == 2:
                while True:
                    try:
                        length = input("\nEnter desired movie duration (in minutes), type 0 to remove time filter, or type 1 to return to filter options: ")

                        if length == "1":
                            break
                        if length == "0":
                            filters["length"] = None  # Reset length filter
                            break

                        length = int(length)

                        if length < 0:
                            print("\nPlease enter a positive number.")
                            continue
                        filters["length"] = length  # Update length filter
                        break
                    except:
                        print("\nPlease enter a valid number.")
            elif selection == 3:
                return
            else:
                print("\nPlease enter a number between 1-3.")
        except:
            print("\nPlease enter a valid number.")

# Main program loop
def main():
    while True:
        try:
            selection = int(input("\nMain Menu:\n(1) Search for a movie\n(2) Apply filters\n(3) Exit program\nEnter your choice: "))

            if selection == 1:
                search_movies()
            elif selection == 2:
                apply_filters()
            elif selection == 3:
                print("\nThank you for using the Movie Recommender! Hope you find a great movie!")
                break
            else:
                print("\nPlease enter a number between 1-3.")
        except:
            print("\nPlease enter a valid number.")

if __name__ == "__main__":
    main()

