#9.2 Three Restaurants
class Restaurant:
	""" The class restaurant tells the user about a resturant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		'''Restaurant take name and cuisine type '''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(f"The name of the restaurant is: {self.restaurant_name} and it serves {self.cuisine_type} type of food.")
			
	def	open_restaurant(self):
		print(f"{self.restaurant_name} is open")
			
restaurant_option = Restaurant("Ruth Chris", "American")
restaurant_option1 = Restaurant("Del Frisco", "Brazilian")
restaurant_option2 = Restaurant("McDonalds", "Fast Food")

restaurant_option.describe_restaurant()
restaurant_option.open_restaurant()
print('\n')
restaurant_option1.describe_restaurant()
restaurant_option1.open_restaurant()
print('\n')
restaurant_option2.describe_restaurant()
restaurant_option2.open_restaurant()
