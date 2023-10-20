'''When one of the files do not appear still display the output of what does appear'''
from pathlib import Path

try:
    dogs_path = Path("dogs.txt")
    dogs_contents = dogs_path.read_text()
    print(f"{dogs_contents}\n")
except FileNotFoundError:
    pass


try:
    cats_path = Path("cats.txt")   
    cats_contents = cats_path.read_text()   
    print(f"{cats_contents}\n")
except FileNotFoundError:
    pass
   

