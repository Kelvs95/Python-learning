alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "red", "points": 15}
alien_2 = {"color": "yellow", "points": 25}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

#```````````````````````````````````````````````````````````````\
#make an empty list for storing aliens
aliens = []

#Make a list of 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5,
                 "speed": "slow"}
    aliens.append(new_alien)

#show the first five aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens you created
print(f"\n Total aliens created: {len(aliens)}")

#_____________________________________________________________
 # List in a Dictionary

pizza_order = {
    'type': 'pepperoni',
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'tomatoes'] #list
}

#Summarize order
print(f"\n You ordered a {pizza_order['type'].title()} pizza with "
      f"{pizza_order['crust']} crust. Toppings include:")

for topping in pizza_order['toppings']:
    print(f"\t {topping.title()} ")

p_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c', 'c++'],
    'edward': ['go', 'java'],
    'phil': ['python', 'heskell'],
}

for name, languages in p_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"{language.title()}")


# Dictionary in a Dictionary
#for i in range(3):
#    print(i)