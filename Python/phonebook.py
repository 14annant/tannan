import csv

with open("phonebook.csv", "a") as file:

    name = input("Name: ")
    number = input("Number: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name":name, "number":number})




'''
file = open("phonebook.csv", "a")

name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close
###
people = {
    "Tom": "1-508-840-1000",
    "David": "1-508-840-1111"
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")
'''
