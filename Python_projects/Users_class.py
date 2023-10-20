#9.3 Users

class Users:
	'''This does what'''
	
	def __init__(self, first_name, last_name, hired_date, department):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.hired_date = hired_date
		self.department = department
		
	def describe_user(self):
		print(f'\n Name: {self.last_name},{self.first_name}\n Department: {self.department}\n Date Hired (mm/yyyy):{self.hired_date}')
		
	def greet_user(self):
		print(f'Thanks {self.first_name} {self.last_name} from the {self.department} for being a loyal employee since {self.hired_date}')
		

employee = Users("Tom", "Annan", "08/2018", "Tech")
employee1 = Users("john", "white", "12/2019", "Customer Service")
employee2 = Users("chris", "brown", "06/2015", "Finance")

employee.describe_user()
employee.greet_user()
print('\n')
employee1.describe_user()
employee1.greet_user()
print('\n')
employee2.describe_user()
employee2.greet_user()
print('\n')
