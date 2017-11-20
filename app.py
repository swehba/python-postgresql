from movie import Movie
from user import User

user = User("Steve")
print(user)

movie = Movie("The Matrix", "sci-fi")
user.movies.append(movie)
print(user.movies)
