class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary


    def give_raise(self, raise_amount = 5000):
        self.raise_amount = raise_amount
        total = raise_amount + self.annual_salary
        return total


john = Employee('tom','annan',100000)
print(john.give_raise())

