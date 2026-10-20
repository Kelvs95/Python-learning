def greet_user():
    print("hello")
    #greeting = input("Welcome, what is your name?")
    #print("Hello, " + greeting)
greet_user()

#Passing information to a function
def greet_user(username):
    print(f"Hello {username.title()}!")

greet_user("tune")

# TIYS
def display_message():
    print("Hi all, I am learning to write a function.")

display_message()

#TIYS
def favorite_book(title):
    print(f"My favorite book is {title.title()}!")

favorite_book("ikigai")

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type.title()}, "
          f"her name is {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("cat", "charlie")

#TIYF
def make_shirt(size, text):
    print(f"Shirt size is {size} and "
          f"text on the shirt is {text.title()}.")

make_shirt("XL", "THIS IS PYHTON") #positional argument
make_shirt(size= "L", text= "Udo di") # Keyword arguments

def describe_city(city, country = "nigeria"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("awka")
describe_city("lagos")
describe_city(city= "toronto", country= "canada")

#TIYS
def get_formatted(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

footballer = get_formatted("Bukayo"
                           , "olanrewaju"
                           , "Saka")
print(footballer)

#TIYS
def get_formatted(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

footballer_name = get_formatted(first_name="Bukayo", last_name="Saka")
print(footballer_name)
footballer_name = get_formatted("Bukayo", "olanrewaju", "Saka")
print(footballer_name)

#Returning a dictionary
def build_person(first_name, last_name):
    person = {'first' : first_name, 'last' : last_name }
    return person

your_person = build_person("Jim", "Ovia")
print(your_person)

#Passing a list
def greet_users(name):
    for user in name:
        message = f"Hello {user.title()}!, Pleased to meet you."
        print(message)
usernames = ['Lori', 'graham', 'billy']
# name or username, doesnt matter here, you can call the function greet_users()
greet_users(usernames)

#Modifying a list
unprinted_designs = ['phone case', 'pendant', 'glasses']
completed_models = []
# Simulate printing each design, until one are left
# Move each design to completed_models after printing

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("printing model: " + current_design)
    completed_models.append(current_design)

#Display all completed models
print("\nThe following models have been printed:")
for model in completed_models:
    print(model)

magicians = ['Merlin', 'Zeddicus', 'Zed']
def show_magicians():
    for magician in magicians:
        print(magician)
show_magicians()

def make_great():
    for magic in magicians:
        print(f"\n{magic.title()} is a green magician.")
make_great()

#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings): # The * tells Python to make an empty tuple
    # called toppings and pack whatever values it
    # receives into this tuple.
    print(toppings)
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

def make_pizza(*toppings):

    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza "
          f"with the following toppings: ")

    for topping in toppings:
        print("- " + topping)

make_pizza(16, "pepperoni")
make_pizza(14, "mushrooms", "green peppers", "extra cheese")

#Arbitrary Keyword Argument
def build_profile(first, last, **user_info):
    #1. Build a dictionary containing everything
    # we know about the user
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("Pat", "Laima",
                             location= "Cairo",
                             occupation= "Engineer" )
print(user_profile)

#Arbitrary Keyword Argument
#Basically trying to use user input to fill in the dictionary
#def build_prof(first, last, **user_info):
    #1. Build a dictionary containing everything
    # we know about the user
    # double * means we can add as much user information to
    # the dictionary as possible
#   profile = {}
#    profile['first_name'] = input("Enter Firstname: ")
#    profile['last_name'] = input("Enter Lastname: ")
#    profile['location'] = input("Enter location: ")
#    profile['occupation'] = input("Enter occupation: ")
    
#    for key, value in user_info.items():
#        profile[key] = value

#    return profile

#user_profile = build_prof("Pat", "Laima")
#print(user_profile)



def sandwich():
    toppings = []
    print("\nEnter 'q' to quit.")

    while True:
        tops = input("Enter a topping: ")
        
        if tops == "q":
            break
        toppings.append(tops)

    return toppings

my_order = sandwich()
print(f"Your sandwich toppings : {my_order}")

def cars(manufacturer, model, **other_infor):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model

    for key, value in other_infor.items():
        car_info[key] = value

    return car_info

my_car = cars("Ford", "F-150", colour= 'dark blue',
              roadworthy = "Yes", tow_package = "True")
print(my_car)