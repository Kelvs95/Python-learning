message = input("Enter a message and i will repeat it:")
print(message)


name = input("Please, enter your name:")
print(f"Hello {name.title()}, Nice to meet you")

# Accepting Integer values
height = input("Please, enter your height:")
height = int(height)

if 175 <= height < 200:
    print("You are above average")
elif height < 175:
    print("You are below average")
else:
    print("You are tall, would you like to play basketball?")

dinner_date = input("Table for how many please? ")
dinner_date = int(dinner_date)

if dinner_date > 8:
    print("I'm sorry, you have to wait for a table")
else:
    print("Your table is ready")

multiples_of_10 =  input("Enter a number:")
multiples_of_10 = int(multiples_of_10)

if multiples_of_10 % 10 == 0:
    print("the value you entered is a multiple of 10")
else:
    print("the value you entered is not a multiple of 10")

# WHILE LOOPS
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\nEnter 'quit' to end the program: "

while True:
    city_name = input(prompt)

    if city_name == "quit":
        break
    else:
        print(f"{city_name.title()}, is a an amazing city")

#Add toppings to your pizza
pizza_toppings = "\nPlease enter your choice toppings:"
pizza_toppings += "\nEnter 'quit' to end: "

while True:
    topping_name = input(pizza_toppings)

    if topping_name == "quit":
        break
    else:
        print(f"{topping_name.title()}, added to your pizza")


# Movie tickets
age = "\nPlease enter your age:"

while True:
    value = input(age)
    value = int(value)

    if value < 3:
        print("Ticket is free")
        break
    elif 3 >= value <= 12:
        print("Ticket is $10")
        break
    else:
        print("Ticket is $15")
        break