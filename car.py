class Car():
    def __init__(self, make, model, year):
        #Initialize the attributes of a car next
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        #return a neatly formatted descriptive name
        car_profile = f"{self.year} {self.make} {self.model} "
        return car_profile

    def read_odometer(self):
        print(f"This {self.make} has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

my_car = Car("Ford", "Mustang", 2020)
my_car2 = Car("Tesla", "Model Y", "2025")
my_car3 = Car("Toyota", "Tacoma", "2026")

print(my_car.describe_car())
my_car.read_odometer()

print(my_car2.describe_car())
# We can modify an attribute by accessing it directly through an instance
my_car2.odometer_reading = 567 #modified instance
my_car2.read_odometer()

print(my_car3.describe_car())
my_car3.update_odometer(150)
my_car3.read_odometer()
