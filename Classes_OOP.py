# When you write a class, you define the
# general behavior that a whole category of objects can have.

#Making an Object from a class is called Instantiation
# You are making an instance of a class.

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def profile(self):
        print(f"{self.name} is {self.age} years old!")

    def sit(self, position = "running"):
        self.position = position
        print(f"{self.name.title()}, {self.age} "
              f"years, is now {self.position}")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

# The methods in this class are, sit(), profile(), roll_over()
# because Sit() requires to know the position of the Dog(), we added another
# argument "Position"

dog1 = Dog("Whiskey", 18)
dog2 = Dog("Paper", 22)
my_dog = Dog("Harry", 24)

#Calling Methods
Dog.profile(dog2)
Dog.sit(dog1)
Dog.roll_over(dog1)
# OR
# Calling Methods
my_dog.sit()
my_dog.roll_over()
dog1.sit()

# RESTAURANT CLASS

class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} restaurant, "
              f"cooks {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} restaurant is open!")

restaurant1 = restaurant("Ceecee's", 'italian')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = restaurant("Arpu's", 'Indian')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

class User():  #Class
    def __init__(self, first_name, last_name):
        #first_name & last_name are attributes
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self, age = 32): #method
        self.age = age
        print(f"{self.first_name}, is {self.age} years old!")

    def height_in_cm(self, height_in_cm = 180):
        self.height_in_cm = height_in_cm
        print(f"{self.first_name} {self.last_name} "
              f"is {self.height_in_cm} cm tall")

user1 = User("John", "Doe") #instances/objects
user1.describe_user()
user1.height_in_cm()

user2 = User("Fidelia", "Doe")
user2.describe_user(age = 56)
user2.height_in_cm(height_in_cm = 170) #methods of the instances/objects


