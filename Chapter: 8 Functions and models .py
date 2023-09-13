#Chapter 8 Functions

def display_message():
	print("In this chapter I will learn to define functions")
	
display_message()

def favorite_book(title):
	print(f"One of my favorite books is {title.title()}")
	
favorite_book(" cat in the hat")

#8.4 Large T-shirts

def make_shirt(size = "Large", text = "I love python"):
	print(f'The text of the shirt is "{text}" and the size is {size.upper()}')

make_shirt()	
make_shirt(size = "medium")
make_shirt(size = "small", text = "I love pizza")

#8.5 cities

def describe_city(city, country = "USA"):
	print(f"{city.title()} is in {country.title()}")

describe_city(city = "accra", country = "ghana")
describe_city("houston")

#8.6 city names

def city_country(city, country):
	print(f"{city.title()}, {country.title()}")

city_country("boston", "USA")
city_country("paris", "france")
city_country("berlin", "germany")

#8.8 User Album

def make_album(artist_name, album_title, songs = None):
	album = {"artist": artist_name.title(),"album": album_title.title(), "song": songs}
	return album
	
while True:
	x = input("Enter you favorite artist and album. \nPress any button to continue. When you are ready to quit enter 'q'")
	if x == "q":
		break
	
	artist_name = input("Enter artist name: \n")
	album_title = input("Enter album title name: \n")
	
	#album = make_album(artist_name, album_title)
	print(make_album(artist_name, album_title))

#8.9 Messages

def show_messages(messages):
	for message in messages:
		print(message) 
		
def send_messages(messages, sent_messages):
	while messages:
		current_message = messages.pop()
		sent_messages.append(current_message)
		print(current_message)
		 
		
messages = ["hello", "hi", "hey"]
sent_messages = []

send_messages(messages, sent_messages)
#below is a copy of a list not the orginal list
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

#8.12 Sandwiches

def make_sandwhices(*items):
	print("Here is the list of your ingredients:")
	for item in items:
		print(f"\t-{item.title()}")
		
		
make_sandwhices("calzone", "bbq chicken")
make_sandwhices("PB&J", "grilled cheese", "ham and cheese")
make_sandwhices("turkey")

#8.13 user profile

def build_profile(first, last, **user_info):
	user_info['first_name'] = first	
	user_info['last_name'] = last
	return user_info
	
user_profile = build_profile('tom','annan', location = 'worcester', field = 'computer science')

print(user_profile)

#8.14 cars

def make_cars(manufacturer, model, **user_info):
	user_info["make"] = manufacturer
	user_info["model_type"] = model
	return user_info
	
car = make_cars("bmw", "530e", color = "black", tow_package = True)
print(car)

		
