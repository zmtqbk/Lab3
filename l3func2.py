#1 task
def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5
#2 task
def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
#3 task
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]
#4 task
def average_imdb_score(movies):
    if len(movies) == 0:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)
#5 task
def average_imdb_by_category(movies, category):
    filtered_movies = movies_by_category(movies, category)
    return average_imdb_score(filtered_movies)


#example 
# Sample movie data
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Testing the functions
print(is_imdb_above_5_5(movies[0]))  # True

print(movies_above_5_5(movies))  
# List of movies with IMDB score above 5.5

print(movies_by_category(movies, "Romance"))  
# List of Romance movies

print(average_imdb_score(movies))  # Average IMDB score for all movies

print(average_imdb_by_category(movies, "Romance"))  
# Average IMDB score for Romance movies
