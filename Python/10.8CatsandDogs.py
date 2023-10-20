

from pathlib import Path

try:
    dogs_path = Path("dogs.txt")
    cats_path = Path("cats.txt")

    dogs_contents = dogs_path.read_text()
    cats_contents = cats_path.read_text()
except FileNotFoundError:
    print("File was not found")
else:
    print(f"{dogs_contents}\n")
    print(f"{cats_contents}\n")