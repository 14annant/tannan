#7.4 Pizza Toppings

toppings = []

prompt = "\nWhat would you like on your pizza?\n"
prompt += "(When done enter 'quit'):"

while True:
	topping = input(prompt)
	if topping == "quit":
		break
	else:
		print(f"Adding {topping} to your pizza!")
		toppings.append(topping)
		continue

print("\nHere is everything on your pizza:")
for i in toppings:
	print(f"\t{i}")

#7.5 Movie Tickets

promt = "\n(when done ordering enter 'quit')\nWelcome to the movies. How old are you?: "
age = True




while age:
	age = input(promt)
	if age == 'quit':
		age = False
		break
	
	age = int(age)
	if age < 3:
		print("Free ticket")
		
	elif age < 12:
		print("Ticket is $12")
		
	else:
		print("Ticket is $15")
		

#7.8 Deli Moving one list to another

sandwhich_orders = ["chicken cutlet", "chicken parm", "italian", "roast beef"]
finished_sandwhiches = []

while sandwhich_orders:
	finished_sandwhich = sandwhich_orders.pop()
	
	print(f"I made you {finished_sandwhich} order")
	finished_sandwhiches.append(finished_sandwhich)

print("\n")
for finished_sandwhich in finished_sandwhiches:
	print(f"Your {finished_sandwhich} has been made")

#7.9 No Pastrami

sandwhich_orders = ["chicken cutlet", "pastrami", "chicken parm", "italian", "pastrami", "roast beef", "pastrami"]
finished_sandwhiches = []

while  "pastrami" in sandwhich_orders:
	sandwhich_orders.remove("pastrami")
	
while sandwhich_orders:
	finished_sandwhich = sandwhich_orders.pop()
	
	print(f"I made you {finished_sandwhich} order")
	finished_sandwhiches.append(finished_sandwhich)

print("\n")
for finished_sandwhich in finished_sandwhiches:
	print(f"Your {finished_sandwhich} has been made")


#7.10 Dream vacation

prompt = "\nIf you could vist one place in the world where would you go? I will display the results of the poll at the end. (Enter quit to end poll)\n"

destinations = []
status = True

while status:
	destination = input(prompt)
	
	if destination == 'quit':
		status = False
		break
		
	else:
		destinations.append(destination.title())
		
print("\nHere all the unique places listed")
destinations = set(destinations)
for destination in sorted(destinations):
	print(destination)
