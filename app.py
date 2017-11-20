from movie import Movie
from user import User

user = User("Steve")
print(user)

movie = Movie("The Matrix", "sci-fi", True)
user.movies.append(movie)
print(f'all movies = {user.movies}')
print(f'watched movies = {user.watched_movies}')
print(f'unwatched movies = {user.unwatched_movies}')

user.save_to_file()
user = User.load_from_file(user.name + ".csv")
print(user)
print(user.movies)
