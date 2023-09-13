#Chapter 8 Functions

def display_message():
	print("In this chapter I will learn to define functions")
	


def favorite_book(title):
	print(f"One of my favorite books is {title.title()}")
	


#8.4 Large T-shirts

def make_shirt(size = "Large", text = "I love python"):
	print(f'The text of the shirt is "{text}" and the size is {size.upper()}')



#8.5 cities

def describe_city(city, country = "USA"):
	print(f"{city.title()} is in {country.title()}")



#8.6 city names

def city_country(city, country):
	print(f"{city.title()}, {country.title()}")


#8.8 User Album

def make_album(artist_name, album_title, songs = None):
	album = {"artist": artist_name.title(),"album": album_title.title(), "song": songs}
	return album
	

#8.9 Messages

def show_messages(messages):
	for message in messages:
		print(message) 
		
def send_messages(messages, sent_messages):
	while messages:
		current_message = messages.pop()
		sent_messages.append(current_message)
		print(current_message)
		 
		

#8.12 Sandwiches

def make_sandwhices(*items):
	print("Here is the list of your ingredients:")
	for item in items:
		print(f"\t-{item.title()}")
		


#8.13 user profile

def build_profile(first, last, **user_info):
	user_info['first_name'] = first	
	user_info['last_name'] = last
	return user_info
	


#8.14 cars

def make_cars(manufacturer, model, **user_info):
	user_info["make"] = manufacturer
	user_info["model_type"] = model
	return user_info
	


		
