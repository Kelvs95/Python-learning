# In Python, square brackets ([]) indicate a list, and individual elements
# in the list are separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())


#If we want to extract starting from the right side of the list or end of list
print(bicycles[-1].title())
print(bicycles[-2].title())

output = "My first bicycle was a " + (bicycles[1].title()) + "."
print(output)

#Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding using .append()
motorcycles.append('ducati')
print(motorcycles)

#Creating an empty list
cities = []
cities.append('Toronto')
cities.append('Paris')
cities.append('London')
cities.append('Lagos')
cities.append('Swansea')

print(cities)

#adding a new city to the list and deciding exactly
#where it should be(position) on the list, use .insert(position, str)

cities.insert(3, 'Accra')
print(cities)

#Removing element from the list use del

del cities[2]
print(cities)

del cities[-3]
print(cities)

#We can also remove an item from a list using pop()
#Pop() removes the last item on the list but still allows you to work with it
popped_cities = cities.pop(-3)
#without specifying the index to pop, the function pops the last item
#it can be useful to get the most recent item purchased
print(cities)
print(popped_cities)

last_visit = "The recent city i visited was " + popped_cities + "."
print(last_visit)

#Removing an item by value
bicycles.remove("trek")
print(bicycles)


#Organizing a list using Sort(), in this case, we are sorting the list
# permanently
phones = ['Iphone', 'Samsung', 'Huawei', 'OnePlus', 'Redmi']
phones.sort()
print(phones)

#To sort a list temporarily
phones1 = ['Iphone', 'Samsung', 'Huawei', 'OnePlus', 'Redmi']

print(sorted(phones1))
print(phones1)
print(phones1[-3])

#finding the length of a list
print(len(phones))
