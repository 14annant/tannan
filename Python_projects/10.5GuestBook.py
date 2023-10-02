'''The purpose of this code is to simulate a guest book. When the user is done the names will appear in a text file'''

from pathlib import Path

path = Path("guest_book.txt")
names = []

while True:
    name_entered = input("Tell me you name when done enter 'quit'\n")
    
    if name_entered == 'quit':
        break
    
    names.append(name_entered)
    print(f"Thank you {name_entered} you have been added to the guestbook!\n")

text = ''
for name in names:
    text += f"{name_entered}\n"
    
path.write_text(text)

