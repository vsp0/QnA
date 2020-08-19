import json


def update_users(users):
    with open('data/users.json', 'w') as f:
        json.dump(users, f, indent=4, sort_keys=True)
