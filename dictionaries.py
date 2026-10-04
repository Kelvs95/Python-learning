# Consider a simple dictinoary
aliens = {'colour': 'green', 'points': 5}
print(aliens['colour'])
print(aliens['points'])

print("you just earned " + str(aliens['points']) + ' points!')

#Adding to a dictionary
aliens['from'] = 'avengers'
aliens['planet'] = 'endgame'

print(aliens)

# Starting with an empty dictionary
alien_o = {}

alien_o['color'] = 'green'
alien_o['points'] = 5

print(alien_o)

#Modifying values in a dictionary

alien_o['color'] = 'yellow'
print('The alien is now color:', alien_o['color'])
print(alien_o)

#-------------------------------------------------------------------
alien_positiion = {"x_position": 23, 'y_position': 30,
                  'speed': 'medium'}
print(f"The original alien position is "
      f"{alien_positiion['x_position']} latitude")

#if the speed changes, let's increment x
if alien_positiion['speed'] == 'slow':
    x_increment = 1
elif alien_positiion['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_positiion['x_position'] = (
        alien_positiion['x_position'] + x_increment)

print(f"The new alien position is {alien_positiion['x_position']}")

########
fav_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(f"\nJen's favorite language is {fav_language['jen'].title()}.")

#### TRY IT YOURSELF
my_friend = {
    'first_name': 'chidera',
    'last_name': 'Ibe',
    'age': 32,
    'city': 'Manilla, Philippines'
}
print(my_friend)

fav_numbers = {
    'ceci': 5,
    'papa': 24,
    'oge': 13,
    'solum': 21
}
print(fav_numbers)

#### Looping through Key-Value Pairs

user_x = {
    'username': 'Paul_xx',
    'firstname': 'Paul',
    'lastname': 'Cubarsi',
}

for key, value in user_x.items():
    print(f"\nkey: {key}")
    print(f"\nvalue: {value}")
    #print(f"\n{key}: {value}")

#-------------------------------------------------------------
print(fav_language)

for name, language in fav_language.items():
    print(f"\n {name.title()}'s favorite language "
          f"is {language.title()}")

# We can always print just the keys or values in a dictionary
for name in fav_language.keys():
    print(f"{name.title()}\n")

for language in fav_language.values():
    print(f"{language.title()}")

friends = ["phil", "sarah"]
for name in fav_language.keys():
    if name in friends:
        print(f"\n Hi {name.title()}!, "
              f"i see your favorite language"
              f" is {fav_language[name].title()}")

# You can sort a dictionary, ideally you just care for the values in
# the keys and values, but you can sort them eg: sort by the time of
# submission.
for name in sorted(fav_language.keys()):
    print(f"\n {name.title()}, thank you for taking the poll.")

#TRY IT YOURSELF

rivers = {'nile':'egypt', 'zambezi': 'zambia', 'orange': 'lesotho'}
for river, country in rivers.items():
    print(f"\n {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(f" {river.title()}")

for country in rivers.values():
    print(f"\n {country.title()}")

#fav language continues
no_poll_yet = ['pat', 'john', 'tony', 'edward']

for names in no_poll_yet:
    if names in fav_language.keys():
        print(f"\n {names.title()}, thank you for taking the poll.")
    else:
        print(f"\n {names.title()}, please take the poll.")


