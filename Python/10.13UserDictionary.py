from pathlib import Path
import json

path = Path('username.json')

if path.exists():
  contents = path.read_text() 
  info = json.loads(contents) 
  print(f"Welcome back, {info['username']}!")
  print(f"\tEmail: {info['email']}\n \tPhone Number: {info['phone_number']}")
else:
  info = dict(username = input("What is your name? "), email = input("What is your email? "), phone_number = input("What is your phone_number? "))
  contents = json.dumps(info) 
  path.write_text(contents)
  print(f"We'll remember the info given when you come back, {info['username']}!")
  print(f"\tEmail: {info['email']}\n \tPhone Number: {info['phone_number']}")
