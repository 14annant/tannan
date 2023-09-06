##4.1
pizzas = ["BBQ", "Cheese", "Pepperoni"]

for pizza in pizzas:
    print(f"\tI love {pizza} pizza")
print("\nThese are my favorite pizzas!\n")

###4.2
animals = ["Dog", "Cat", "Turtle"]


for animal in animals:
    print(f"\tA {animal} would make such a great pet")
print("\nHonestly any of these would make a great pet\n")

#for i in range(1,21):
#    print(i)

'''
##4.4 one million
million = list(range(1,1000001))
print(min(million))
print(max(million))
print(sum(million))

##4.6 odd numbers
odd_numbers = range(1,20,2)

for i in odd_numbers:
    print(i)

##4.7 threes
threes = list(range(3,31,3))

for three in threes:
    print(three)
##4.8 cubes
cubes = list(range(1,11))
for cube in cubes:
    print(f"{cube} cubed is {cube**3}")

##4.9 Cube comprehension
cubes2 = [cube**3 for cube in range(1,11)]
print(cubes2)


##4.10 slicing
odd_numbers = list(range(1,20,2))
print(f"the first three items from the list are {odd_numbers[:3]}\n")
print(f"the middle three items from the list are {odd_numbers[3:6]}\n")
print(f"the last three items from the list are {odd_numbers[-3:]}\n")
for i in odd_numbers:
    print(i)

##4.11 my pizza, your pizza
pizzas = ["BBQ", "Cheese", "Pepperoni"]
friends_pizzas = pizzas[:]

pizzas.append("Hawaian")
friends_pizzas.append("Meat Lovers")


for pizza in pizzas:
    print("My favorite pizza is " + pizza)
print("\n")

for pizza in friends_pizzas:
    print("My favorite pizza is " + pizza)

##4.13 tuples this is made for lists or dimmensions that should be changed
buffets = ("fried rice", "ice cream", "noodles", "chicken", "spare ribs")
for buffet in buffets:
    print(buffet)
print("These items are in the original list\n")


buffets = ("general tso", "ice cream", "noodles", "chicken", "orange chicken" )
for buffet in buffets:
    print(buffet)
print("These items are in the new list\n")
'''