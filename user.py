class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f'<User "{self.name}">'
