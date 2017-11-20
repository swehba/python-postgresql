from user import User
import json

user = User('Steve')
user.add_movie('The Matrix', 'sci-fi')
user.add_movie('The Interview', 'comedy')

FILE_NAME = 'my_file.txt'

with open(FILE_NAME, 'w') as f:
    json.dump(user.json, f, indent=4)

with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)

print(json.dumps(user.json, indent=4))
