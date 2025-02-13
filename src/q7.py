class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, initMake, initModel, initYear):
        self.make = initMake
        self.model = initModel
        self.year = initYear
        
    def describe_car(self):
        print("Year: {0}, Make: {1}, Model: {2}".format(self.year, self.make, self.model))


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
my_car = Car('Toyota', 'Corolla', 2020)
my_car.describe_car()