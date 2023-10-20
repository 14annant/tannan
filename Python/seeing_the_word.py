#places I have visted. Testing sorting through lists using functions such as reverse(), sorted()

places_visited = ["miami", " Tokoyo", "Cartagena", "Toronto ", "London", " Paris ", "washington dC", "Maryland ", "worcester" , "Boston", "Miami", "Orlando"]

places = []
for i in places_visited:
    places.append(i.strip().title())

print(f"\nPlaces I've been in order (A-Z) {sorted(places)}\n")

duplice = input("tell me the duplicate: ")

places.remove("Miami")

print(f"\nSorry looks like I have a duplicate {sorted(places)}\n")
result = input("Would you like to see this in desc order (Z-A)?: \n\tType:Y or N: ")
result = result.lower()

while result != None:
    if result in ['y','yes']:
        print(sorted(places, reverse= True))
        break
    elif result in ['no','n']:
        print(f"Here's the places I been to by order {places.reverse()}")
        break

print("Tell me 3 places you been to by order from earliest to latest")
user_places = []
result1 = user_places.append(input("Place 1: "))
result2 = user_places.append(input("Place 2: "))
result3 = user_places.append(input("Place 3: "))

print(f"Cool {user_places[0]} is an amazing places to go to as a first trip!")
print(f"Your most recent visit was {user_places.pop()} awesome!")




