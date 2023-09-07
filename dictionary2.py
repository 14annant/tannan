'''
#6.1 Persons dictionary
person = {
    "first_name" : "Tom",
    "last_name" : "Annan",
    "age" : "27",
    "city" : "orlando",
}
print(person)

#6.2 Favorite number
fav_num = {
    "john" : "8",
    "kobe" : "24",
    "lebron" : "6",
    "jordan" : "23",
    "jason" : "12",
}
for i in fav_num:
    print(f"{i} favorite number is {fav_num[i]}")
 
 #6.4 glossary

glossary = {
    "tuple" : "similiar to a list but once created this values cannot be edited",
    "list" : "a group of strings or numbers represent a value within a list",
    "loop" : "iteration of code",
    "error" : "A message that the terminal or compiler throws out at you when it is unable to compile code due to a mistake",
    "break" : "Breaking out a code block and moving on to what comes next",
}

for i in sorted(glossary):
    print(f"{i.title()}:\n\t{glossary[i].title()}\n")

#6.5 rivers
rivers = {
    "nile" : "egypt",
    "mississipi" : "america",
    "amazon" : "south america",
    "mississipi" : "america",
}

#sorted() removes duplicates
for river, country in sorted(rivers.items()):
    print(f"{river.title()} runs through {country.title()}")
 
print("\n")    
for river, country in sorted(rivers.items()):
    print(river)
    
print("\n")    
for river, country in sorted(rivers.items()):
    print(country)

#6.6 polling
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
}

first_names = ["edward", "tom","jen","frank","dan"]
first_names.append("chris")

for first_name in first_names:
    if first_name in favorite_languages.keys():
        print(f"Thanks for taking the poll {first_name}")
    else:
        print(f"Please take the poll {first_name}")
    
#6.7 people
person_0 = {
    "first_name" : "Tom",
    "last_name" : "Annan",
    "age" : "27",
    "city" : "orlando",
}

person_1 = {
    "first_name" : "george",
    "last_name" : "brown",
    "age" : "60",
    "city" : "cleveland",
}

person_2 = {
    "first_name" : "john",
    "last_name" : "white",
    "age" : "30",
    "city" : "boston",
}
people = [person_0,person_1,person_2]

for person in people:
    print(f"\n{person}")

#6.9 favorite places
# the [] are necessary if not put will produce a weird output
favorite_places = {"tom":["toronto", "columbia", "chicago"],
    "chris":["miami"],
    "john":["boston", "washington dc"],
    
}


for name, city in favorite_places.items():
    print(f"\n{name.title()}s favorite places to visit are:")
    for citys in city:
        print("\t" + citys.title())
    
'''

#6.10 Favorite numbers
fav_num = {
    "john" : ["8", "32"],
    "kobe" : ["24", "8"],
    "lebron" : ["6", "23"],
    "jordan" : ["23", "45"],
    "jason" : ["12", "55"],
}
for name, number in fav_num.items():
    print(f"\n{name.title()} favorite number is:")
    for num in number:
        print(f"\t{num}")