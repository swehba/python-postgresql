from movie import Movie
from user import User

user = User("Steve")
print(user)

movie = Movie("The Matrix", "sci-fi", True)
user.movies.append(movie)
print(f'all movies = {user.movies}')
print(f'watched movies = {user.watched_movies}')
print(f'unwatched movies = {user.unwatched_movies}')
