##import this
#3.4 guest list
guests = ["James Brown", "Michael Jackson", "Drake"]
message = ", is invited to my dinner"
for i in guests:
    print(i + message)
print(f"Guest total is : {len(guests)}")
print("\n")

#3.5 changing guest list
print("Drake can’t make it")
guests = ["James Brown", "Michael Jackson", "Drake"]
busy_guest = guests.remove( "Drake")

print(f"Old list: {guests[0:]}")

guests.append("Barry white")
print(f"Current list: {guests[0:]}")

for i in guests:
    print(i + message)
print(f"Guest total is : {len(guests)}")
print("\n")

#3.6 More guest insert new dinner guest

print("Drake can’t make it")
guests = ["James Brown", "Michael Jackson", "Drake"]
busy_guest = "Drake"
guests.remove(busy_guest)
print(guests)

guests.append("Barry white")
print(guests)

for i in guests:
    print(i + message)
print("Found a bigger table adding new guest")

guests.insert(0, "50 Cent")
guests.insert(1, "Miley Cyrus")
guests.append("Beyoncé")

print(guests)
for i in guests:
    print(i + message)
print(f"Guest total is : {len(guests)}")
print("\n")

#3.7 shrink the guest list down to 2 people

print("Drake can’t make it, so I am adding someone new")
guests = ["James Brown", "Michael Jackson", "Drake"]
busy_guest = "Drake"
guests.remove(busy_guest)
print(guests)

guests.append("Barry white")
print(guests)

for i in guests:
    print(i + message)
print("\nFound a bigger table adding new guest")

guests.insert(0, "50 Cent")
guests.insert(1, "Miley Cyrus")
guests.append("Beyoncé")

print(f"Current list: {guests[0:]}")
for i in guests:
    print(i + message)
print(f"Guest total is : {len(guests)}")
## this is 3.7
print("\nSorry but I can only invite 2 people now")
print(f"Current list: {guests[0:]}")

pop_guest0 = guests.pop()
print("\nsorry but you were the last one invited, " + pop_guest0)

pop_guest1 = guests.pop()
print("sorry but you were the second to last one invited, " + pop_guest1)

pop_guest2 = guests.pop()
print("sorry but you were the one of the last ones invited, " + pop_guest2)

pop_guest3 = guests.pop()
print("sorry but you were the one of the last ones invited, " + pop_guest3)

print(guests[0] + " and " + guests[1] + " your are still welcomed.")

print(f"New list: {guests[0:]}")
del guests[1]
del guests[0]

print(guests)
print(f"Guest total is : {len(guests)}")