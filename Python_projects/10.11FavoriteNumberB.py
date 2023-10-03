from pathlib import Path
import json


path = Path("favorite_number.json")
contents = path.read_text()
reader = json.loads(contents)

print(f"I know your favorite number! It's {reader}.")
