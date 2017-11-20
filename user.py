from movie import Movie
import csv
import re


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

    def save_to_file(self):
        with open(self.name + '.csv', 'w', newline='') as csvfile:
            field_names = ['name', 'genre', 'watched']
            writer = csv.DictWriter(csvfile, field_names)
            writer.writeheader()
            for movie in self.movies:
                writer.writerow({'name': movie.name,
                                 'genre': movie.genre,
                                 'watched': str(movie.watched)})

    @classmethod
    def load_from_file(cls, filename):
        pattern = re.compile(r'(.*)\.csv')
        match = pattern.match(filename)
        if not match:
            return None

        user = cls(match.group(1))
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movie = Movie(row['name'], row['genre'], bool(row['watched']))
                user.movies.append(movie)

        return user
