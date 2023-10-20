from pathlib import Path
import json


path = Path("favorite_number.json")
fav_num = input("What's your favorite numer? \n")
contents = json.dumps(fav_num)
path.write_text(contents)

