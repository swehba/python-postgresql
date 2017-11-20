from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f'<User "{self.name}">'

    @property
    def watched_movies(self):
        return [movie for movie in self.movies if movie.watched]

    @property
    def unwatched_movies(self):
        return [movie for movie in self.movies if not movie.watched]

    def add_movie(self, name, genre, watched=False):
        movie = Movie(name, genre, watched)
        self.movies.append(movie)
        return movie

    def delete_movie(self, name):
        self.movies = [movie for movie in self.movies if movie.name == name]
