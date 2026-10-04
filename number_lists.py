# Using range() function
#
from statistics import mean

val = range(0, 5)
for vals in val:
    print(vals)

#using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

#for even numbers between 1 and 10
even_numbers = list(range(2,11,2))
print(even_numbers)

#odd numbers
odd_numbers = list(range(1,11,2))
print(odd_numbers)

#squares
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

## SIMPLE STATISTICS

digits = list(range(0,10))

print(min(digits))
print(max(digits))
print(sum(digits))
print(mean(digits))

cubes = []
for cub in range(1,7):
    cubes.append(cub**3)

print(cubes)

three = []
for three_ms in range(3,30):
    three.append(three_ms*3)

print(three)

#WORKING WITH A PART OF A LIST (slicing)

arsenal_players = ['saka', 'martin', 'kai', 'timber', 'Calafiori']
print(arsenal_players)
print(arsenal_players[0:2])
print(arsenal_players[2:4])
print(arsenal_players[-1])
print(arsenal_players[-2:])

#Looping through a slice

print('Here are the list of top three arsenal players:') 
for players in arsenal_players[:3]:

    print(players.title())

my_foods = ['Pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print('my favourite foods are:')
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friends_food)

for food in my_foods[:1]:
    print('My favourite food is:')
    print(food)

for foods in friends_food[-1:]:
    print("\nMy friends favourite meal is:")
    print(foods)

# TUPLE (List that cannot change)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250  #it will give an error because its a tuple
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


buffet = ('rice', 'salad', 'chicken dinner', 'casserole')
for dishes in buffet:
    print(dishes)

# buffet[1] = 'ugba'

buffet = ('beans', 'coleslaw', 'chicken dinner', 'casserole')
print("\nModified buffet includes these meals:")
for modified_buffet in buffet:
    print(modified_buffet)
