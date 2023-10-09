'''Program checks if a user is saved, if not it will create the user if so it will welcome the user.'''
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        username = info['username']
        return username
    else:
        return None
def get_new_username(path):
    """Prompt for a new username."""
    info ={"username": "USER"}
    info['username'] = input("What is your name? ")
    username = info['username']
    contents = json.dumps(info)
    path.write_text(contents)
    return username
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    message = input(f"Is your name {username}? (Y/N)").upper()

    if message == 'Y':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()