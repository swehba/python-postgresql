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
