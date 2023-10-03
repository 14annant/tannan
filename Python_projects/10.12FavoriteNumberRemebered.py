#Looks or writes a file that contains your favorite number. If the file exist number is displayed if not number is written in the file
from pathlib import Path
import json


path = Path("favorite_numbera.json")

if path.exists():
    contents = path.read_text()
    reader = json.loads(contents)
    
    print(f"I know your favorite number! It's {reader}.")

else:
    fav_num = input("What's your favorite numer? \n")
    contents = json.dumps(fav_num)
    path.write_text(contents)
