# Grant Merrill --- Z23813057

# === Problem 4: CSV Files ===
# imdb-top-rated.csv:    Rank, Title, Year, IMDB Rating
# imdb-top-grossing.csv: Rank, Title, Year, USA Box Office
# imdb-top-casts.csv:    Title, Year, Director, Actor 1, Actor 2, Actor 3, Actor 4, Actor 5
import csv
from operator import itemgetter

# === display_top_collaborations Function ===
def display_top_collaborations(rated, casts):
    """Display the top director/actor collaborations from the top-rated movies."""
    
    # This function only needs the titles of the top rated movies, so extract them using list comprehension. 
    movies = [title for rank, title, year, rating in rated]
    
    # Using a list comprehension to keep only cast entries whose movie also appears in the top-rated movie list.
    # The title of entries in casts is compared to titles in movies, ensuring only movies on the top rated list are used.
    ranked_movies = [(title, director, a1, a2, a3, a4, a5) 
              for title, year, director, a1, a2, a3, a4, a5 in casts 
              for movie_title in movies
              if title == movie_title]
    
    # Building off the last comprehension, use another one to create a pair for each actor with their director.
    # The new pairs are stored in pairing for the next step.
    pairing = [(director, actor) 
               for title, director, a1, a2, a3, a4, a5 in ranked_movies
               for actor in [a1, a2, a3, a4, a5]]
    
    # Taken from the third approach to count occurences in a dictionary.
    counts = {}
    for pair in pairing:
        counts[pair] = counts.get(pair, 0) + 1
        
    
    # Another list comprehension, this time to pack the director, actor, and count into a tuple.
    results = [(director, actor, value) for (director, actor), value in counts.items()]
    
    # Taken from the 'More on Sorting' section of 7.3.2 List Methods
    results = sorted(results, key=itemgetter(2), reverse=True)
    
    
    print("=== Director/Actor Collaborations in the Top 250 Ranked Movies ===")
    print("{:>12} {:>19} {:>17}".format("Director", "Actor", "Number"))
    print("=" * 50)
    for index, (director, actor, num) in enumerate(results):
        if index >= 10:
            break
        print(f"{index + 1:>2}. {director:<22} {actor:<16} {num}")
        
    print("\n")
        
# === display_top_actors Fuction ===
def  display_top_actors(grossing, casts):
    """Display the actors ranked by their total box office earnings."""
    
    # List comprehension to collect only the relevant information from the top grossing CSV file.
    movie_grossing = [(title, money)
                      for rank, title, year, money in grossing]
    
    # List comprehension to create tuples containing each movie's actors and box office earnings.
    actor_earnings = [(a1, a2, a3, a4, a5, money)
                      for title, year, director, a1, a2, a3, a4, a5 in casts
                      for movie_title, money in movie_grossing
                      if title == movie_title]
    
    # List comprehension that creates a pair (actor, money) for each actor with the money made from a movie.
    pairing = [(actor, int(money))
               for a1, a2, a3, a4, a5, money in actor_earnings
               for actor in [a1, a2, a3, a4, a5]]
    
    # Using the same third method from the book used in the other function to iterate through the pairs. 
    # Each actor is assigned as a key, and every occurrence has the saved earnings added to that actor's total.
    earnings = {}
    for pair in pairing:
        if pair[0] in earnings:
            earnings[pair[0]] += pair[1]
        else:
            earnings[pair[0]] = pair[1]
            
    
        
        
    # From 'Code Listing 9.4', sorting the dictionary by using list comprehension to reverse the key, value tuple pairs.    
    earnings_list = [(value, key) for key, value in earnings.items()]
        
    # Sorting the list using the .sort(reverse=True) method in 'Code Listing 9.4'.
    earnings_list.sort(reverse=True)
    
    # Reverse the order of the key, value pairs again after the sorting
    earnings = [(value, key) for key, value in earnings_list]
    
    # Displaying only the top 10 grossing actors
    print("===== Top Grossing Actors (2014) =====")
    print("{:>9} {:>25}".format("Actor", "Earnings"))
    print("=" * 38)
    for index, (actor, earning) in enumerate(earnings):
        if index >= 10:
            break
        print(f"{index + 1:>2}. {actor:<22} {earning:<16}")
        
        

# === main() Function ===
def main():
    """Read the IMDb CSV files and test Parts a and b."""
    print("Grant Merrill --- Z23813057\n\n")
    
    # Open all of the CSV files.
    top_rated = open('imdb-top-rated.csv', "r")
    top_grossing = open('imdb-top-grossing.csv', "r")    
    top_casts = open('imdb-top-casts.csv', "r", encoding = 'utf-8')
    
    # Read all the files and skip the header.
    reader_rated = csv.reader(top_rated)
    next(reader_rated)
    
    reader_grossing = csv.reader(top_grossing)
    next(reader_grossing)
    
    reader_casts = csv.reader(top_casts)
    next(reader_casts)
    
    # Initialize a list for each file's data.
    rated = []
    grossing = []
    casts = []
    
    # Pack each line into a tuple and add it to its list.
    for line in reader_rated:
        rated.append(tuple(line))
        
    for line in reader_grossing:
        grossing.append(tuple(line))
        
    for line in reader_casts:
        casts.append(tuple(line))
        
        
    # Testing the code for Part a
    display_top_collaborations(rated, casts)
    
    # Testing the code for Part b
    display_top_actors(grossing, casts)
        
        
        
# === Main ===
main()